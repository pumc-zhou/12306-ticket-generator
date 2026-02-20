# -*- coding: utf-8 -*-
"""
邮件解析模块

负责解析 12306 购票成功邮件，提取车票信息。
"""

from .email_parser import parse_email

__all__ = ["parse_email"]
