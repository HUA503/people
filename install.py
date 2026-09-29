#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
People Agent Skills 一键跨平台安装脚本
支持快速将本仓库中的技能安装到当前电脑的各大 Agent 宿主中。
"""

import argparse
import os
import shutil
import sys
from pathlib import Path

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

REPO_ROOT = Path(__file__).resolve().parent
SKILLS_DIR = REPO_ROOT / "skills"

DEFAULT_TARGETS = {
    "agentskills": Path.home() / ".agents" / "skills",
    "claude-code": Path.home() / ".claude" / "skills",
    "antigravity": Path.home() / ".gemini" / "config" / "skills",
    "codex": Path.home() / ".agents" / "skills",
}


def list_available_skills():
    if not SKILLS_DIR.exists():
        return []
    return sorted([d.name for d in SKILLS_DIR.iterdir() if d.is_dir() and (d / "SKILL.md").exists()])


def install_skill(skill_name: str, target_dir: Path, force: bool = False):
    src = SKILLS_DIR / skill_name
    dst = target_dir / skill_name

    if not src.exists():
        print(f"[-] 技能 '{skill_name}' 不存在于 skills/ 目录下。")
        return False

    target_dir.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        if not force:
            print(f"[!] 目标已存在: {dst} (如需覆盖请添加 --force 参数)")
            return False
        shutil.rmtree(dst)

    shutil.copytree(src, dst)
    print(f"[+] 已成功安装 [{skill_name}] -> {dst}")
    return True


def main():
    parser = argparse.ArgumentParser(description="People Agent Skills 一键安装工具")
    parser.add_argument("--skill", type=str, help="指定要安装的技能名称（如 wu-junjin 或 tan-denghuan）")
    parser.add_argument("--all", action="store_true", help="安装本仓库内的所有技能")
    parser.add_argument("--list", action="store_true", help="列出当前仓库所有可用技能")
    parser.add_argument(
        "--host",
        type=str,
        default="auto",
        choices=["auto", "agentskills", "claude-code", "antigravity", "codex"],
        help="指定目标宿主 (默认 auto 会自动检测已存在的宿主环境并安装)",
    )
    parser.add_argument("--dest", type=str, help="自定义安装的目标父目录")
    parser.add_argument("--force", "-f", action="store_true", help="覆盖已存在的同名技能")

    args = parser.parse_args()

    available = list_available_skills()

    if args.list:
        print(f"仓库中包含 {len(available)} 个可用技能:")
        for s in available:
            print(f"  - {s}")
        return

    skills_to_install = []
    if args.skill:
        if args.skill not in available:
            print(f"[-] 未找到技能: {args.skill}")
            print(f"可选技能列表: {', '.join(available)}")
            sys.exit(1)
        skills_to_install = [args.skill]
    else:
        skills_to_install = available

    # Determine targets
    target_dirs = []
    if args.dest:
        target_dirs.append(Path(args.dest).expanduser())
    elif args.host != "auto":
        target_dirs.append(DEFAULT_TARGETS[args.host])
    else:
        # Auto mode: install to standard ~/.agents/skills
        target_dirs.append(DEFAULT_TARGETS["agentskills"])
        # If Antigravity config directory exists on machine, install there too
        if (Path.home() / ".gemini").exists():
            target_dirs.append(DEFAULT_TARGETS["antigravity"])
        # If Claude directory exists, install there too
        if (Path.home() / ".claude").exists():
            target_dirs.append(DEFAULT_TARGETS["claude-code"])

    # Deduplicate resolved target paths
    unique_targets = []
    for t in target_dirs:
        try:
            resolved = t.resolve()
        except Exception:
            resolved = t
        if resolved not in unique_targets:
            unique_targets.append(resolved)

    print(f"==> 准备安装 {len(skills_to_install)} 个技能到 {len(unique_targets)} 个目标宿主目录...")
    for target in unique_targets:
        print(f"==> 目标目录: {target}")
        for s in skills_to_install:
            install_skill(s, target, force=args.force)

    print("\n[OK] 安装流程完成！可在对应平台直接使用 /<skill-name> 开始对话。")


if __name__ == "__main__":
    main()
