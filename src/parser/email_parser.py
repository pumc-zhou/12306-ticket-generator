# -*- coding: utf-8 -*-
"""
12306 邮件解析器

解析 12306 购票成功邮件的 HTML 内容，提取车票相关信息。

提取的信息包括:
    - 乘车人姓名
    - 身份证号（脱敏）
    - 车次
    - 出发站/到达站
    - 出发日期/时间
    - 座位信息（车厢号、座位号、席别）
    - 票价
    - 订单号
"""

import re
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

from bs4 import BeautifulSoup


@dataclass
class TicketInfo:
    """车票信息数据类"""
    
    # 乘车人信息
    passenger_name: str = ""           # 乘车人姓名
    id_number: str = ""                # 身份证号（脱敏）
    
    # 车次信息
    train_number: str = ""             # 车次号，如 G1234
    train_date: str = ""               # 乘车日期，如 2024-01-15
    
    # 站点信息
    departure_station: str = ""        # 出发站
    arrival_station: str = ""          # 到达站
    departure_time: str = ""           # 出发时间，如 08:30
    arrival_time: str = ""             # 到达时间，如 12:45
    
    # 座位信息
    coach_number: str = ""             # 车厢号
    seat_number: str = ""              # 座位号
    seat_class: str = ""               # 席别，如 二等座、一等座
    
    # 票务信息
    ticket_price: float = 0.0          # 票价
    order_number: str = ""             # 订单号
    
    # 其他信息
    ticket_gate: str = ""              # 检票口
    remarks: str = ""                  # 备注


@dataclass
class ParseResult:
    """解析结果"""
    tickets: List[TicketInfo] = field(default_factory=list)
    raw_html: str = ""
    parse_time: str = field(default_factory=lambda: datetime.now().isoformat())


def parse_email(html_file_path: str) -> ParseResult:
    """
    解析 12306 购票成功邮件
    
    Args:
        html_file_path: 邮件 HTML 文件路径
        
    Returns:
        ParseResult: 包含车票信息的解析结果
        
    Raises:
        FileNotFoundError: 文件不存在
        ValueError: HTML 格式不正确或无法解析
    """
    # 读取 HTML 文件
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # 使用 BeautifulSoup 解析
    soup = BeautifulSoup(html_content, "lxml")
    
    result = ParseResult(raw_html=html_content)
    
    # TODO: 实现具体的解析逻辑
    # 这里需要根据 12306 邮件的实际 HTML 结构来提取信息
    # 不同时期的邮件模板可能有所不同，需要适配多种格式
    
    ticket = _extract_ticket_info(soup)
    if ticket:
        result.tickets.append(ticket)
    
    return result


def _extract_ticket_info(soup: BeautifulSoup) -> Optional[TicketInfo]:
    """
    从 HTML 中提取车票信息
    
    Args:
        soup: BeautifulSoup 对象
        
    Returns:
        TicketInfo 或 None
    """
    ticket = TicketInfo()
    
    # TODO: 根据实际邮件结构实现提取逻辑
    # 以下为示例代码，需要根据真实邮件调整选择器
    
    # 示例：提取车次号
    # train_elem = soup.select_one(".train-number")
    # if train_elem:
    #     ticket.train_number = train_elem.get_text(strip=True)
    
    # 示例：提取站点信息
    # departure_elem = soup.select_one(".departure-station")
    # if departure_elem:
    #     ticket.departure_station = departure_elem.get_text(strip=True)
    
    return ticket


def _parse_datetime(date_str: str) -> Optional[datetime]:
    """
    解析日期时间字符串
    
    Args:
        date_str: 日期时间字符串
        
    Returns:
        datetime 对象或 None
    """
    patterns = [
        "%Y年%m月%d日",
        "%Y-%m-%d",
        "%Y/%m/%d",
    ]
    
    for pattern in patterns:
        try:
            return datetime.strptime(date_str.strip(), pattern)
        except ValueError:
            continue
    
    return None


def _sanitize_id_number(id_number: str) -> str:
    """
    脱敏身份证号
    
    Args:
        id_number: 原始身份证号
        
    Returns:
        脱敏后的身份证号，如 1101**********1234
    """
    if len(id_number) >= 18:
        return id_number[:4] + "*" * 10 + id_number[-4:]
    return id_number
