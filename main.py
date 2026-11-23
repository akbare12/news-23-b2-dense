#!/usr/bin/env python3
"""Copy the pre-rendered front page to /output/entry.png.

The entry image is rendered at build time (draw.py, PIL) and committed as
entry.png. At run time this program only copies it to the output directory,
using the Python standard library only, so it runs identically on the
judge's machine. No network access.
"""
import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    src_size = os.path.getsize(SRC)
    dst_size = os.path.getsize(dst)
    src_hash = sha256_of(SRC)
    dst_hash = sha256_of(dst)
    if src_size != dst_size or src_hash != dst_hash:
        raise SystemExit(
            "copy verification failed: src %d bytes %s, dst %d bytes %s"
            % (src_size, src_hash, dst_size, dst_hash)
        )
    print("wrote", dst, dst_size, "bytes, sha256", dst_hash)


if __name__ == "__main__":
    main()
