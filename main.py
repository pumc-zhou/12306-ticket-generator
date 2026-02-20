#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
12306 车票生成器 - 项目入口

本程序用于解析 12306 购票成功邮件，并生成仿真火车票 PDF。

使用方法:
    python main.py --input <邮件HTML文件> --output <输出PDF路径>

示例:
    python main.py --input tests/emails/sample.html --output output/ticket.pdf
"""

import argparse
import os
import sys

from src.parser.email_parser import parse_email
from src.renderer.typst_renderer import render_ticket


def main():
    """主函数：解析命令行参数并执行票据生成流程"""
    parser = argparse.ArgumentParser(
        description="12306 车票生成器 - 从购票邮件生成仿真车票 PDF",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--input", "-i",
        required=True,
        help="12306 购票成功邮件的 HTML 文件路径"
    )
    parser.add_argument(
        "--output", "-o",
        default="output/ticket.pdf",
        help="生成的 PDF 输出路径 (默认: output/ticket.pdf)"
    )
    parser.add_argument(
        "--template", "-t",
        default="templates/ticket.typ",
        help="Typst 模板文件路径 (默认: templates/ticket.typ)"
    )
    
    args = parser.parse_args()
    
    # 检查输入文件是否存在
    if not os.path.exists(args.input):
        print(f"错误: 输入文件不存在 - {args.input}")
        sys.exit(1)
    
    # 确保输出目录存在
    output_dir = os.path.dirname(args.output)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    try:
        # 步骤1: 解析邮件内容
        print(f"正在解析邮件: {args.input}")
        ticket_data = parse_email(args.input)
        
        # 步骤2: 使用 Typst 渲染生成 PDF
        print(f"正在生成车票: {args.output}")
        render_ticket(ticket_data, args.template, args.output)
        
        print(f"✓ 车票生成成功: {args.output}")
        
    except Exception as e:
        print(f"错误: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
