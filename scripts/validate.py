#!/usr/bin/env python3
"""Validate a skills-only ChatGPT/Codex plugin package before submission.

Checks mirror the public submission limits documented at
https://developers.openai.com/plugins/deploy/submission
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)

MAX_NAME = 64
MAX_DISPLAY_NAME = 30
MAX_SHORT_DESCRIPTION = 30
MAX_LONG_DESCRIPTION = 4000
MAX_DEVELOPER_NAME = 80
MAX_DEFAULT_PROMPTS = 3
MAX_DEFAULT_PROMPT_LEN = 128
MAX_CAPABILITIES = 20
MAX_SKILL_DESCRIPTION = 1024

FORBIDDEN_PATHS = [".app.json", "hooks", ".mcp.json", "mcp.json"]
REQUIRED_URL_FIELDS = ["websiteURL", "supportURL", "privacyPolicyURL", "termsOfServiceURL"]
ASSET_FIELDS = ["composerIcon", "composerIconDark", "logo", "logoDark"]


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []

    def check(self, condition: bool, message: str) -> None:
        if not condition:
            self.errors.append(message)


def load_manifest(report: Report) -> dict | None:
    manifest_path = ROOT / "plugin.json"
    if not manifest_path.exists():
        report.errors.append("plugin.json is missing")
        return None
    try:
        return json.loads(manifest_path.read_text())
    except json.JSONDecodeError as exc:
        report.errors.append(f"plugin.json is not valid JSON: {exc}")
        return None


def check_identity(manifest: dict, report: Report) -> None:
    name = manifest.get("name", "")
    report.check(bool(NAME_RE.match(name)), f"name must be kebab-case: {name!r}")
    report.check(len(name) <= MAX_NAME, f"name exceeds {MAX_NAME} chars")
    report.check(bool(SEMVER_RE.match(manifest.get("version", ""))), "version must be semver x.y.z")
    report.check(
        manifest.get("$schema") == "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
        "$schema must be the Agent Plugins 1.0.0 schema",
    )


def check_length(report: Report, obj: dict, field: str, limit: int) -> None:
    value = obj.get(field)
    report.check(isinstance(value, str) and value.strip() != "", f"interface.{field} is required")
    if isinstance(value, str):
        report.check(len(value) <= limit, f"interface.{field} exceeds {limit} chars ({len(value)})")


def check_asset_path(report: Report, field: str, value: str) -> None:
    report.check(value.startswith("./"), f"{field} must start with ./ : {value!r}")
    report.check((ROOT / value).exists(), f"{field} file not found: {value}")


def check_interface(manifest: dict, report: Report) -> dict:
    openai_ext = manifest.get("extensions", {}).get("com.openai", {})
    interface = openai_ext.get("interface")
    if not isinstance(interface, dict):
        report.errors.append("extensions.com.openai.interface is required")
        return openai_ext

    check_length(report, interface, "displayName", MAX_DISPLAY_NAME)
    check_length(report, interface, "shortDescription", MAX_SHORT_DESCRIPTION)
    check_length(report, interface, "longDescription", MAX_LONG_DESCRIPTION)
    check_length(report, interface, "developerName", MAX_DEVELOPER_NAME)
    report.check(bool(interface.get("category")), "interface.category is required")

    for field in REQUIRED_URL_FIELDS:
        value = interface.get(field, "")
        report.check(value.startswith("https://"), f"interface.{field} must be an https URL")

    prompts = interface.get("defaultPrompt", [])
    if isinstance(prompts, str):
        prompts = [prompts]
    report.check(len(prompts) <= MAX_DEFAULT_PROMPTS, "too many defaultPrompt entries")
    report.check(len(set(prompts)) == len(prompts), "defaultPrompt entries must be unique")
    for prompt in prompts:
        report.check(len(prompt) <= MAX_DEFAULT_PROMPT_LEN, f"defaultPrompt too long: {prompt[:40]}...")
        report.check("@" not in prompt, f"defaultPrompt must not contain @mentions: {prompt[:40]}")

    capabilities = interface.get("capabilities", [])
    report.check(len(capabilities) <= MAX_CAPABILITIES, "too many capabilities")

    for field in ASSET_FIELDS:
        if field in interface:
            check_asset_path(report, f"interface.{field}", interface[field])
    for shot in interface.get("screenshots", []):
        check_asset_path(report, "interface.screenshots[]", shot)

    report.check("logo" in interface, "interface.logo is required for submission")
    return openai_ext


def check_onboarding(openai_ext: dict, report: Report) -> None:
    onboarding = openai_ext.get("onboardingSkill")
    if onboarding is None:
        return
    report.check(onboarding.startswith("./skills/"), "onboardingSkill must point inside ./skills/")
    report.check((ROOT / onboarding).exists(), f"onboardingSkill not found: {onboarding}")


def parse_frontmatter(text: str) -> dict[str, str] | None:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip().strip('"').strip("'")
    return fields


def check_skills(report: Report) -> None:
    skills_dir = ROOT / "skills"
    if not skills_dir.is_dir():
        report.errors.append("skills/ directory is missing")
        return
    skill_dirs = [p for p in skills_dir.iterdir() if p.is_dir()]
    report.check(len(skill_dirs) > 0, "skills/ contains no skills")
    for skill_dir in skill_dirs:
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            report.errors.append(f"{skill_dir.name}: SKILL.md missing")
            continue
        fields = parse_frontmatter(skill_md.read_text())
        if fields is None:
            report.errors.append(f"{skill_dir.name}: SKILL.md lacks YAML frontmatter")
            continue
        report.check(fields.get("name") == skill_dir.name, f"{skill_dir.name}: frontmatter name must match folder")
        description = fields.get("description", "")
        report.check(description != "", f"{skill_dir.name}: description is required")
        report.check(
            len(description) <= MAX_SKILL_DESCRIPTION,
            f"{skill_dir.name}: description exceeds {MAX_SKILL_DESCRIPTION} chars",
        )


def check_forbidden(report: Report) -> None:
    for rel in FORBIDDEN_PATHS:
        report.check(not (ROOT / rel).exists(), f"{rel} blocks submission; remove it from the package")


def main() -> int:
    report = Report()
    manifest = load_manifest(report)
    if manifest is not None:
        check_identity(manifest, report)
        openai_ext = check_interface(manifest, report)
        check_onboarding(openai_ext, report)
    check_skills(report)
    check_forbidden(report)

    if report.errors:
        print("FAIL")
        for error in report.errors:
            print(f"  - {error}")
        return 1
    print("PASS: plugin package is valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
