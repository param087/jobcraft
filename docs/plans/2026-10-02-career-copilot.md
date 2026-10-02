# JobCraft Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build and package a skills-only ChatGPT/Codex plugin ("JobCraft") ready for directory submission.

**Architecture:** Portable Agent Plugins package: `plugin.json` manifest + six `skills/*/SKILL.md` + assets. A Python validation script enforces manifest limits and SKILL.md frontmatter so packaging errors are caught before upload.

**Tech Stack:** Markdown, JSON, Python 3 (stdlib only) for validation, `zip` for packaging.

---

### Task 1: Validation script (test first)

**Files:**
- Create: `scripts/validate.py`

Step 1: Write `scripts/validate.py` that asserts:
- `plugin.json` parses; `name` kebab-case ≤64; `version` semver.
- `extensions.com.openai.interface`: `displayName` ≤30, `shortDescription` ≤30, `longDescription` ≤4000, `developerName` ≤80, `category` present, `defaultPrompt` ≤3 items each ≤128, all `*URL` start with `https://`.
- Every referenced asset path starts with `./` and exists.
- `onboardingSkill` points to an existing `SKILL.md`.
- Each `skills/*/SKILL.md` has YAML frontmatter with `name` (matches folder) and `description` (non-empty, ≤1024).
- No `.app.json`, `hooks/`, `.mcp.json`, `mcp.json` present.

Step 2: Run `python3 scripts/validate.py` → expect FAIL (no plugin.json yet).
Step 3: Commit.

### Task 2: Manifest and assets

**Files:**
- Create: `plugin.json`, `assets/logo.png`, `assets/icon.png`, `assets/icon.svg`

Step 1: Write `plugin.json` per design doc.
Step 2: Generate a 512×512 PNG logo and icon with Python (stdlib `zlib`/`struct` PNG writer) — no PIL dependency.
Step 3: Run validator → expect FAIL only on missing skills.
Step 4: Commit.

### Task 3: Skills

**Files:** `skills/{get-started,tailor-resume,cover-letter,interview-prep,offer-negotiation,application-tracker}/SKILL.md` plus `references/` and `assets/` where listed in the design.

Step 1: Write each SKILL.md following authoring rules.
Step 2: Run validator → PASS.
Step 3: Commit.

### Task 4: Local marketplace

**Files:**
- Create: `.agents/plugins/marketplace.json` (repo marketplace)
- Append entry to `~/.agents/plugins/marketplace.json` (personal)

Step 1: Write both; restart ChatGPT desktop; verify plugin appears.
Step 2: Commit repo file only.

### Task 5: README + packaging

**Files:**
- Create: `README.md` (test matrix), `scripts/package.sh`

Step 1: `package.sh` runs validator then zips `plugin.json skills assets README.md` to `dist/jobcraft-<version>.zip`.
Step 2: Run → zip exists, `unzip -l` lists expected files only.
Step 3: Commit.

### Task 6: Submission

Manual: verify identity at platform.openai.com → Plugins → Upload ZIP → fix findings → Submit → Publish.
