# -*- coding: utf-8 -*-
"""
邮件解析器单元测试
"""

import os
import pytest
from pathlib import Path

from src.parser.email_parser import (
    parse_email,
    TicketInfo,
    ParseResult,
    _sanitize_id_number,
    _parse_datetime,
)


# 测试文件目录
TESTS_DIR = Path(__file__).parent
EMAILS_DIR = TESTS_DIR / "emails"


class TestTicketInfo:
    """TicketInfo 数据类测试"""
    
    def test_default_values(self):
        """测试默认值"""
        ticket = TicketInfo()
        assert ticket.passenger_name == ""
        assert ticket.train_number == ""
        assert ticket.ticket_price == 0.0
    
    def test_custom_values(self):
        """测试自定义值"""
        ticket = TicketInfo(
            passenger_name="张三",
            train_number="G1234",
            departure_station="北京南",
            arrival_station="上海虹桥",
        )
        assert ticket.passenger_name == "张三"
        assert ticket.train_number == "G1234"


class TestSanitizeIdNumber:
    """身份证号脱敏测试"""
    
    def test_full_id_number(self):
        """测试完整身份证号脱敏"""
        result = _sanitize_id_number("110101199001011234")
        assert result == "1101**********1234"
        assert len(result) == 18
    
    def test_short_id_number(self):
        """测试短身份证号"""
        result = _sanitize_id_number("123456")
        assert result == "123456"  # 不做处理


class TestParseDatetime:
    """日期解析测试"""
    
    def test_chinese_format(self):
        """测试中文日期格式"""
        result = _parse_datetime("2024年01月15日")
        assert result is not None
        assert result.year == 2024
        assert result.month == 1
        assert result.day == 15
    
    def test_dash_format(self):
        """测试横线日期格式"""
        result = _parse_datetime("2024-01-15")
        assert result is not None
        assert result.year == 2024
    
    def test_invalid_format(self):
        """测试无效日期格式"""
        result = _parse_datetime("invalid date")
        assert result is None


class TestParseEmail:
    """邮件解析测试"""
    
    @pytest.mark.skipif(
        not (EMAILS_DIR / "sample.html").exists(),
        reason="示例邮件文件不存在"
    )
    def test_parse_sample_email(self):
        """测试解析示例邮件"""
        result = parse_email(str(EMAILS_DIR / "sample.html"))
        assert isinstance(result, ParseResult)
        assert result.raw_html != ""
    
    def test_file_not_found(self):
        """测试文件不存在的情况"""
        with pytest.raises(FileNotFoundError):
            parse_email("nonexistent_file.html")
