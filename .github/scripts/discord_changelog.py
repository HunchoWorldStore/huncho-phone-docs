"""Posts a product's newest changelog entry to Discord when its changelog.md changes.

One post per product, each to its own webhook (repo secrets):
    DISCORD_WEBHOOK_PHONE, DISCORD_WEBHOOK_GAMEPACK, DISCORD_WEBHOOK_NPCPOLICE, DISCORD_WEBHOOK_JOBCENTER,
    DISCORD_WEBHOOK_BOOKBAGS
A product without its own secret uses DISCORD_WEBHOOK, if set. No webhook = skipped.

Optional repo variable DOCS_URL = your GitBook site (e.g. https://docs.example.com): the post links to the
product's docs there. Without it, the post links to the changelog on GitHub.

Only posts when the newest entry (the first "## " section) is new or was edited, so fixing a typo in an
older entry doesn't post anything.
"""
import json
import os
import re
import subprocess
import sys
import urllib.request

PRODUCTS = [
    {
        "key": "PHONE", "name": "Huncho Phone", "changelog": "changelog.md",
        "docs_path": "huncho-phone", "banner": "assets/banner.png", "color": 0x7B6BFF,   # banner blue-purple
    },
    {
        "key": "GAMEPACK", "name": "Huncho World Game Pack", "changelog": "huncho-world-game-pack/changelog.md",
        "docs_path": "huncho-world-game-pack", "banner": "huncho-world-game-pack/assets/banner.png", "color": 0xFFC94A,   # banner gold
    },
    {
        "key": "NPCPOLICE", "name": "Huncho NPC Police", "changelog": "huncho-npc-police/changelog.md",
        "docs_path": "huncho-npc-police", "banner": "huncho-npc-police/assets/banner.png", "color": 0xFF4364,   # banner "POLICE" red
    },
    {
        "key": "JOBCENTER", "name": "Huncho Job Center", "changelog": "huncho-job-center/changelog.md",
        "docs_path": "huncho-job-center", "banner": "huncho-job-center/assets/banner.png", "color": 0x22E4FF,   # banner neon cyan
    },
    {
        "key": "BOOKBAGS", "name": "Huncho Designer Bookbags", "changelog": "huncho-designer-bookbags/changelog.md",
        "docs_path": "huncho-designer-bookbags", "banner": "huncho-designer-bookbags/assets/banner.png", "color": 0x5F97EA,   # banner blue
    },
]

REPO = os.environ.get("GITHUB_REPOSITORY", "")
BRANCH = os.environ.get("GITHUB_REF_NAME", "main")
BEFORE = os.environ.get("BEFORE_SHA", "")
DOCS_URL = os.environ.get("DOCS_URL", "").rstrip("/")


def git_show(rev, path):
    try:
        return subprocess.run(["git", "show", f"{rev}:{path}"], capture_output=True, text=True, check=True).stdout
    except subprocess.CalledProcessError:
        return None


def newest_entry(text):
    """-> (version, body) of the first '## ' section, or (None, None)."""
    if not text:
        return None, None
    m = re.search(r"^##\s+(.+?)\s*$", text, re.M)
    if not m:
        return None, None
    rest = text[m.end():]
    nxt = re.search(r"^##\s+", rest, re.M)
    body = rest[: nxt.start()] if nxt else rest
    return m.group(1).strip(), body.strip()


def to_discord(body):
    out = []
    for line in body.splitlines():
        line = re.sub(r"\\([_*`\[\]()#.!-])", r"\1", line)          # GitBook escapes like \_
        line = re.sub(r"\[([^\]]+)\]\((?!https?://)[^)]*\)", r"\1", line)   # relative doc links -> plain text
        m = re.match(r"^(\s*)[*-]\s+(.*)$", line)
        if m:
            indent = "  " * (len(m.group(1)) // 2)
            line = f"{indent}• {m.group(2)}"
        out.append(line)
    text = "\n".join(out).strip()
    if len(text) > 3900:
        text = text[:3900].rsplit("\n", 1)[0] + "\n…"
    return text


def post(webhook, payload):
    req = urllib.request.Request(
        webhook, data=json.dumps(payload).encode(), method="POST",
        headers={"Content-Type": "application/json", "User-Agent": "huncho-docs-changelog"},
    )
    with urllib.request.urlopen(req, timeout=20) as r:
        return r.status


def main():
    changed = set(sys.argv[1:])
    failed = False
    for p in PRODUCTS:
        if p["changelog"] not in changed:
            continue
        webhook = os.environ.get(f"DISCORD_WEBHOOK_{p['key']}") or os.environ.get("DISCORD_WEBHOOK")
        if not webhook:
            print(f"{p['name']}: no webhook secret, skipped")
            continue
        version, body = newest_entry(git_show("HEAD", p["changelog"]))
        if not version:
            print(f"{p['name']}: no '## version' entry found, skipped")
            continue
        old = newest_entry(git_show(BEFORE, p["changelog"])) if BEFORE and set(BEFORE) != {"0"} else (None, None)
        if old == (version, body):
            print(f"{p['name']}: newest entry unchanged, skipped")
            continue
        edited = old[0] == version
        if DOCS_URL:
            link = f"{DOCS_URL}/{p['docs_path']}".rstrip("/")
        else:
            link = f"https://github.com/{REPO}/blob/{BRANCH}/{p['changelog']}"
        embed = {
            "title": f"{p['name']} {version}" + (" (updated)" if edited else ""),
            "url": link,
            "description": to_discord(body) or "See the changelog.",
            "color": p["color"],
            "footer": {"text": "Full changelog and docs: click the title"},
        }
        if p["banner"]:
            embed["image"] = {"url": f"https://raw.githubusercontent.com/{REPO}/{BRANCH}/{p['banner']}"}
        try:
            status = post(webhook, {"embeds": [embed], "allowed_mentions": {"parse": []}})
            print(f"{p['name']} {version}: posted ({status})")
        except Exception as e:  # keep going for the other products
            print(f"{p['name']} {version}: post failed: {e}")
            failed = True
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
