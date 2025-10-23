#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

github：https://github.com/ifraise/extract_directory_files

提取目录中的文件。从多个目录中提取文件进行汇总。

usage:
    python flatten_dirs.py                   # 扫描当前目录，输出到 ./../_flattened
    python flatten_dirs.py /data/abc         # 扫描 /data/abc，输出到 /data/_flattened
    python flatten_dirs.py . /tmp/all        # 扫描当前目录，输出到 /tmp/all
"""
import shutil
import argparse
from pathlib import Path
from collections import defaultdict

def flatten(root: Path, out: Path):
    out.mkdir(parents=True, exist_ok=True)
    counter = defaultdict(int)
    total = 0

    for file in root.rglob('*'):
        if not file.is_file():
            continue
        name = file.name
        counter[name] += 1
        if counter[name] > 1:
            stem = file.stem
            suffix = file.suffix
            name = f"{stem}({counter[name] - 1}){suffix}"

        dst = out / name
        shutil.move(str(file), str(dst))
        total += 1
        print(f"[+] {file}  ->  {dst}")

    print(f"\n[*] 完成！共移动 {total} 个文件到 {out} \(^o^)/")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="扁平化提取所有文件到单一目录")
    parser.add_argument("src", nargs="?", default=".", help="要扫描的根目录（默认当前目录）")
    parser.add_argument("dst", nargs="?", help="输出目录（默认根目录同级 _flattened）")
    args = parser.parse_args()

    src = Path(args.src).resolve()
    if not src.exists():
        exit(f"[-] (灬ꈍ ꈍ灬) 源目录不存在: {src}")

    dst = Path(args.dst) if args.dst else src.parent / "_flattened"
    flatten(src, dst)