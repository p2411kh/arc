#!/usr/bin/env python3
"""arc - единая обёртка над tar, zip и unzip.

    arc -t <аргументы tar>     ->  tar   <аргументы>
    arc -z <аргументы zip>     ->  zip   <аргументы>
    arc -u <аргументы unzip>   ->  unzip <аргументы>
"""
import os
import shutil
import sys

TOOLS = {"-t": "tar", "-z": "zip", "-u": "unzip"}

HELP = """arc - tar, zip и unzip в одной команде

Использование:
  arc -t [флаги tar]    например: arc -t czf out.tar.gz dir/
                                  arc -t xf out.tar.gz -C dest/
                                  arc -t tf out.tar.gz
  arc -z [флаги zip]    например: arc -z -r out.zip dir/ file.txt
  arc -u [флаги unzip]  например: arc -u out.zip -d dest/
                                  arc -u -l out.zip
  arc -h                эта справка

Всё после -t / -z / -u передаётся в соответствующую программу без изменений.
"""


def main() -> None:
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(HELP)
        sys.exit(0 if args else 1)

    flag, rest = args[0], args[1:]
    tool = TOOLS.get(flag)
    if tool is None:
        sys.exit(f"arc: неизвестный флаг '{flag}'. Смотри: arc -h")

    path = shutil.which(tool)
    if path is None:
        sys.exit(f"arc: '{tool}' не найден в PATH (на NixOS: nix-shell -p {tool})")

    os.execv(path, [tool, *rest])  # заменяем процесс, код возврата = как у tool


if __name__ == "__main__":
    main()
