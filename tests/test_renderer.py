# -*- coding: utf-8 -*-
"""
Typst 渲染器单元测试
"""

import pytest
from pathlib import Path

from src.renderer.typst_renderer import (
    check_typst_installation,
    get_typst_version,
    _convert_to_dict,
)
from src.parser.email_parser import TicketInfo, ParseResult


class TestConvertToDict:
    """数据转换测试"""
    
    def test_convert_ticket_info(self):
        """测试转换 TicketInfo"""
        ticket = TicketInfo(
            passenger_name="李四",
            train_number="D5678",
            ticket_price=299.5,
        )
        result = _convert_to_dict(ticket)
        
        assert isinstance(result, dict)
        assert result["passenger_name"] == "李四"
        assert result["train_number"] == "D5678"
        assert result["ticket_price"] == 299.5
    
    def test_convert_parse_result(self):
        """测试转换 ParseResult"""
        ticket = TicketInfo(passenger_name="王五")
        parse_result = ParseResult(tickets=[ticket])
        
        result = _convert_to_dict(parse_result)
        
        assert isinstance(result, dict)
        assert "tickets" in result
        assert len(result["tickets"]) == 1
        assert result["tickets"][0]["passenger_name"] == "王五"


class TestTypstInstallation:
    """Typst 安装检测测试"""
    
    def test_check_installation_returns_bool(self):
        """测试安装检测返回布尔值"""
        result = check_typst_installation()
        assert isinstance(result, bool)
    
    def test_get_version_returns_string(self):
        """测试版本获取返回字符串"""
        result = get_typst_version()
        assert isinstance(result, str)
