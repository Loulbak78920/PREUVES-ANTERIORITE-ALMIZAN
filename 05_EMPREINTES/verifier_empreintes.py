#!/usr/bin/env python3
"""Recalcule les empreintes SHA-256 du depot. Sortie ASCII, code 0/1."""
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
MANIFEST = os.path.join(HERE, "MANIFESTE_SHA256.json")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    with open(MANIFEST, encoding="utf-8") as f:
        data = json.load(f)
    expected = {e["chemin"]: e for e in data["fichiers"]}
    ok = mismatch = missing = 0
    for rel, entry in sorted(expected.items()):
        path = os.path.join(ROOT, rel)
        if not os.path.isfile(path):
            print("MISSING %s" % rel)
            missing += 1
            continue
        got = sha256(path)
        if got != entry["sha256"]:
            print("MISMATCH %s attendu=%s obtenu=%s" % (rel, entry["sha256"], got))
            mismatch += 1
        elif os.path.getsize(path) != entry["octets"]:
            print("MISMATCH_SIZE %s" % rel)
            mismatch += 1
        else:
            ok += 1
    found = set()
    for root, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d != ".git"]
        for name in files:
            rel = os.path.relpath(os.path.join(root, name), ROOT).replace(os.sep, "/")
            if rel in ("05_EMPREINTES/MANIFESTE_SHA256.json",) or rel.startswith(".git/"):
                continue
            found.add(rel)
    extra = sorted(found - set(expected))
    for rel in extra:
        print("EXTRA %s" % rel)
    print("OK=%d MISMATCH=%d MISSING=%d EXTRA=%d" % (ok, mismatch, missing, len(extra)))
    if mismatch or missing or extra:
        print("RESULT FAIL")
        return 1
    print("RESULT OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
