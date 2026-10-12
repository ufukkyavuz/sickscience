"""Turn a prompts/batch-*.md file into Higgsfield MCP requests.

Each concept is a '## <ID> — ...' heading followed by a ``` code block. In the prompt,
{@ss-name} is an element mention; it becomes <<<uuid>>> (tools/hf_elements.json), which is
the form generate_image / generate_image_batch accept in params.prompt.

usage: python3 tools/hf_prompt.py prompts/batch-41-discount-new-scenes.md [ID ...] > requests.json
Output: [{"index": n, "id": "E1", "params": {model, prompt, aspect_ratio, resolution}}]
Defaults follow CLAUDE.md: nano_banana_pro, 9:16 master, 2k.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ELEMENTS = json.load(open(os.path.join(HERE, "hf_elements.json")))


def parse(md_path):
    text = open(md_path, encoding="utf-8").read()
    out = []
    for m in re.finditer(r"^## (\S+) [—-].*?\n(.*?)```\n(.*?)```", text, re.S | re.M):
        out.append((m.group(1), m.group(3).strip()))
    return out


def resolve(prompt):
    def sub(m):
        name = m.group(1)
        if name not in ELEMENTS:
            sys.exit(f"unknown element @{name} — add it to tools/hf_elements.json")
        return f"<<<{ELEMENTS[name]}>>>"
    return re.sub(r"\{@([a-z0-9-]+)\}", sub, prompt)


if __name__ == "__main__":
    md, wanted = sys.argv[1], set(sys.argv[2:])
    reqs = []
    for i, (cid, prompt) in enumerate(parse(md)):
        if wanted and cid not in wanted:
            continue
        reqs.append({"index": i, "id": cid, "params": {
            "model": "nano_banana_pro", "prompt": resolve(prompt),
            "aspect_ratio": "9:16", "resolution": "2k"}})
    json.dump(reqs, sys.stdout, ensure_ascii=False, indent=1)
