"""
parser.py — 12306 邮件解析模块

负责从 12306 发送的购票成功通知邮件（HTML 格式）中提取结构化票务信息，
供后续的 Typst 渲染模块使用。
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


@dataclass
class TicketInfo:
    """存储单张车票的关键信息。"""

    passenger: str = ""          # 乘客姓名
    id_number: str = ""          # 证件号（脱敏后）
    train_no: str = ""           # 车次，如 G1234
    departure: str = ""          # 出发站
    destination: str = ""        # 到达站
    departure_time: str = ""     # 出发日期时间，如 2026-01-01 08:00
    seat_type: str = ""          # 座位类型，如 二等座
    seat_no: str = ""            # 座位号，如 05车08D号
    ticket_type: str = ""        # 票价类型，如 成人票
    price: str = ""              # 票价，如 553.0元
    order_no: str = ""           # 订单号


def parse_email(html_source: str) -> list[TicketInfo]:
    """从 12306 邮件 HTML 源码中解析车票信息列表。

    Args:
        html_source: 邮件的完整 HTML 字符串。

    Returns:
        解析出的 TicketInfo 列表，每张票对应一个元素。
    """
    # TODO: 实现具体的 HTML 解析逻辑（BeautifulSoup / lxml）
    raise NotImplementedError("parse_email() 尚未实现")


def parse_email_file(path: str | Path) -> list[TicketInfo]:
    """从本地 HTML 文件中读取并解析车票信息。

    Args:
        path: HTML 文件路径。

    Returns:
        解析出的 TicketInfo 列表。
    """
    html_source = Path(path).read_text(encoding="utf-8")
    return parse_email(html_source)
