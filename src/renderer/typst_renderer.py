# -*- coding: utf-8 -*-
"""
Typst 渲染器

将解析后的车票数据传递给 Typst 模板，生成 PDF 文件。

依赖:
    - Typst 命令行工具 (https://typst.app)
"""

import json
import os
import subprocess
import tempfile
from pathlib import Path
from typing import Any, Dict

# 获取项目根目录
PROJECT_ROOT = Path(__file__).parent.parent.parent


def render_ticket(ticket_data: Any, template_path: str, output_path: str) -> None:
    """
    使用 Typst 渲染车票 PDF
    
    Args:
        ticket_data: 车票数据（ParseResult 对象）
        template_path: Typst 模板文件路径
        output_path: 输出 PDF 文件路径
        
    Raises:
        FileNotFoundError: 模板文件不存在
        RuntimeError: Typst 渲染失败
    """
    # 检查模板文件
    template_file = Path(template_path)
    if not template_file.is_absolute():
        template_file = PROJECT_ROOT / template_path
    
    if not template_file.exists():
        raise FileNotFoundError(f"模板文件不存在: {template_file}")
    
    # 将车票数据转换为 JSON
    data_dict = _convert_to_dict(ticket_data)
    
    # 创建临时数据文件
    with tempfile.NamedTemporaryFile(
        mode="w",
        suffix=".json",
        encoding="utf-8",
        delete=False
    ) as data_file:
        json.dump(data_dict, data_file, ensure_ascii=False, indent=2)
        data_file_path = data_file.name
    
    try:
        # 调用 Typst 编译
        _compile_typst(template_file, data_file_path, output_path)
    finally:
        # 清理临时文件
        if os.path.exists(data_file_path):
            os.remove(data_file_path)


def _convert_to_dict(ticket_data: Any) -> Dict[str, Any]:
    """
    将车票数据转换为字典格式
    
    Args:
        ticket_data: ParseResult 对象
        
    Returns:
        字典格式的数据
    """
    if hasattr(ticket_data, "__dict__"):
        # 如果是数据类，转换为字典
        result = {}
        for key, value in ticket_data.__dict__.items():
            if hasattr(value, "__dict__"):
                result[key] = _convert_to_dict(value)
            elif isinstance(value, list):
                result[key] = [
                    _convert_to_dict(item) if hasattr(item, "__dict__") else item
                    for item in value
                ]
            else:
                result[key] = value
        return result
    return ticket_data


def _compile_typst(template_path: Path, data_path: str, output_path: str) -> None:
    """
    调用 Typst 命令行工具编译 PDF
    
    Args:
        template_path: Typst 模板文件路径
        data_path: JSON 数据文件路径
        output_path: 输出 PDF 路径
        
    Raises:
        RuntimeError: 编译失败
    """
    # 确保输出目录存在
    output_dir = Path(output_path).parent
    if not output_dir.exists():
        output_dir.mkdir(parents=True)
    
    # 构建 Typst 命令
    # 通过环境变量或命令行参数传递数据文件路径
    cmd = [
        "typst",
        "compile",
        str(template_path),
        output_path,
        "--input", f"data={data_path}",
        "--font-path", str(PROJECT_ROOT / "assets" / "fonts"),
    ]
    
    # 执行命令
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=str(PROJECT_ROOT)
        )
        
        if result.returncode != 0:
            error_msg = result.stderr or result.stdout or "未知错误"
            raise RuntimeError(f"Typst 编译失败: {error_msg}")
            
    except FileNotFoundError:
        raise RuntimeError(
            "未找到 Typst 命令。请确保已安装 Typst 并添加到系统 PATH。\n"
            "安装说明: https://github.com/typst/typst#installation"
        )


def check_typst_installation() -> bool:
    """
    检查 Typst 是否已安装
    
    Returns:
        True 如果 Typst 已安装
    """
    try:
        result = subprocess.run(
            ["typst", "--version"],
            capture_output=True,
            text=True
        )
        return result.returncode == 0
    except FileNotFoundError:
        return False


def get_typst_version() -> str:
    """
    获取 Typst 版本号
    
    Returns:
        版本号字符串，如 "typst 0.10.0"
    """
    try:
        result = subprocess.run(
            ["typst", "--version"],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except FileNotFoundError:
        pass
    return "未安装"
