# -*- coding: utf-8 -*-
"""
Typst 渲染模块

负责调用 Typst 将车票数据渲染为 PDF。
"""

from .typst_renderer import render_ticket

__all__ = ["render_ticket"]
