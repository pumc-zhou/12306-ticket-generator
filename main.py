#!/usr/bin/env python3
"""
main.py — 12306 电子客票生成器入口

用法示例：
    python main.py --email tests/emails/sample.html --output ticket.pdf
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="从 12306 购票通知邮件生成仿真 PDF 电子客票"
    )
    parser.add_argument(
        "--email",
        required=True,
        type=Path,
        help="12306 邮件的 HTML 源文件路径（参见 tests/emails/ 目录）",
    )
    parser.add_argument(
        "--output",
        default="ticket.pdf",
        type=str,
        help="输出 PDF 文件名（保存在 output/ 目录，默认：ticket.pdf）",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    from src.parser.parser import parse_email_file
    from src.renderer.renderer import render_ticket

    print(f"[1/3] 解析邮件：{args.email}")
    tickets = parse_email_file(args.email)
    if not tickets:
        print("未从邮件中解析到任何车票信息，请检查 HTML 文件格式。", file=sys.stderr)
        return 1

    for i, ticket in enumerate(tickets, start=1):
        filename = args.output if len(tickets) == 1 else f"{Path(args.output).stem}_{i}.pdf"
        print(f"[2/3] 渲染第 {i}/{len(tickets)} 张票 → {filename}")
        output_path = render_ticket(ticket.__dict__, output_filename=filename)
        print(f"[3/3] 已生成：{output_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
