"""
renderer.py — Typst 渲染封装模块

负责将解析后的车票数据填充到 Typst 模板，并调用 Typst CLI 生成最终的 PDF 文件。
"""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

# 项目根目录（renderer.py 的上两级）
_ROOT = Path(__file__).resolve().parents[2]
_TEMPLATE = _ROOT / "templates" / "ticket.typ"
_OUTPUT_DIR = _ROOT / "output"


def render_ticket(ticket_data: dict, output_filename: str = "ticket.pdf") -> Path:
    """将车票数据渲染为 PDF。

    Args:
        ticket_data: 包含票务字段的字典，键名与 ticket.typ 模板中的参数一致。
        output_filename: 输出 PDF 的文件名（相对于 output/ 目录）。

    Returns:
        生成的 PDF 文件路径。

    Raises:
        FileNotFoundError: 若 Typst 未安装或模板文件不存在。
        subprocess.CalledProcessError: 若 Typst 编译失败。
    """
    _OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = _OUTPUT_DIR / output_filename

    # 将数据序列化为 JSON，通过 Typst 的 --input 参数传入模板
    data_json = json.dumps(ticket_data, ensure_ascii=False)

    cmd = [
        "typst",
        "compile",
        "--input", f"data={data_json}",
        str(_TEMPLATE),
        str(output_path),
    ]

    # TODO: 实现完整的数据注入与调用逻辑，取消下方注释以启用 Typst 编译
    # subprocess.run(cmd, check=True)
    # return output_path
    raise NotImplementedError("render_ticket() 尚未实现")
