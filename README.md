# 12306 车票生成器

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Typst](https://img.shields.io/badge/Typst-0.10+-green.svg)](https://typst.app/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> 🚄 从 12306 购票成功邮件生成仿真火车票 PDF

本项目可以解析中国铁路 12306 购票成功的邮件通知，并使用 [Typst](https://typst.app) 排版系统生成高质量的仿真火车票 PDF 文件。

## ✨ 功能特性

- 📧 **邮件解析**：自动提取 12306 购票邮件中的车票信息
- 🎨 **高质量排版**：使用 Typst 现代排版系统，支持中文字体
- 📄 **PDF 输出**：生成清晰、可打印的车票 PDF
- 🔧 **可定制样式**：灵活的模板系统，可自定义票面样式

## 📁 项目结构

```
12306-ticket-generator/
├── assets/                     # 静态资源
│   ├── fonts/                  # 自定义字体（思源黑体、方正等）
│   └── backgrounds/            # 票面底纹背景图 (SVG/PNG)
├── src/                        # 核心代码
│   ├── parser/                 # 邮件解析模块 (Python)
│   │   ├── __init__.py
│   │   └── email_parser.py     # 邮件解析器实现
│   └── renderer/               # Typst 调用封装
│       ├── __init__.py
│       └── typst_renderer.py   # Typst 渲染器实现
├── templates/                  # Typst 模板文件
│   ├── ticket.typ              # 核心排版逻辑
│   └── styles.typ              # 颜色、间距等样式定义
├── tests/                      # 测试用例
│   ├── emails/                 # 12306 邮件 HTML 源码示例
│   │   └── sample.html         # 示例邮件文件
│   ├── test_parser.py          # 解析器测试
│   └── test_renderer.py        # 渲染器测试
├── output/                     # 生成的 PDF 存放处
├── requirements.txt            # Python 依赖
├── main.py                     # 项目入口
├── .gitignore                  # Git 忽略配置
├── LICENSE                     # 开源许可证
└── README.md                   # 项目说明文档
```

## 🚀 快速开始

### 环境要求

- **Python** 3.8 或更高版本
- **Typst** 0.10 或更高版本

### 安装步骤

#### 1. 克隆项目

```bash
git clone https://github.com/yourusername/12306-ticket-generator.git
cd 12306-ticket-generator
```

#### 2. 安装 Python 依赖

```bash
# 创建虚拟环境（推荐）
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

#### 3. 安装 Typst

**Windows (使用 winget)**
```bash
winget install --id Typst.Typst
```

**macOS (使用 Homebrew)**
```bash
brew install typst
```

**Linux**
```bash
# 从 GitHub Releases 下载
# https://github.com/typst/typst/releases
```

或访问 [Typst 官方安装指南](https://github.com/typst/typst#installation)

#### 4. 配置字体（可选）

将中文字体文件放入 `assets/fonts/` 目录。推荐字体：

- [思源黑体 (Source Han Sans)](https://github.com/adobe-fonts/source-han-sans)
- [Noto Sans SC](https://fonts.google.com/noto/specimen/Noto+Sans+SC)

### 使用方法

#### 基本用法

```bash
python main.py --input <邮件HTML文件> --output <输出PDF路径>
```

#### 示例

```bash
# 使用示例邮件生成车票
python main.py --input tests/emails/sample.html --output output/ticket.pdf

# 指定自定义模板
python main.py --input email.html --output ticket.pdf --template templates/ticket.typ
```

#### 命令行参数

| 参数 | 简写 | 说明 | 默认值 |
|------|------|------|--------|
| `--input` | `-i` | 12306 邮件 HTML 文件路径 | (必填) |
| `--output` | `-o` | 输出 PDF 文件路径 | `output/ticket.pdf` |
| `--template` | `-t` | Typst 模板文件路径 | `templates/ticket.typ` |

## 📧 获取 12306 邮件

1. 登录您的邮箱（购票时绑定的邮箱）
2. 搜索来自 12306 的购票成功邮件
3. 查看邮件原始 HTML 源码
4. 保存为 `.html` 文件

**注意**：不同邮箱客户端获取源码的方式不同：
- **Gmail**：点击"更多" → "显示原始邮件"
- **Outlook**：点击"..." → "查看消息源"
- **QQ邮箱**：点击"更多" → "显示邮件原文"

## 🎨 自定义样式

### 修改颜色方案

编辑 `templates/styles.typ`：

```typst
// 主色调 - 修改为您喜欢的颜色
#let primary-color = rgb("#1E88E5")
#let accent-color = rgb("#1565C0")
```

### 修改票面尺寸

```typst
// 标准火车票尺寸
#let ticket-width = 85mm
#let ticket-height = 54mm
```

### 修改字体

```typst
#let main-font = (
  "Source Han Sans SC",  // 优先使用
  "Microsoft YaHei",     // 备选
)
```

## 🧪 运行测试

```bash
# 运行所有测试
pytest

# 运行特定测试文件
pytest tests/test_parser.py

# 显示详细输出
pytest -v

# 生成覆盖率报告
pytest --cov=src --cov-report=html
```

## 📋 开发计划

- [x] 项目框架搭建
- [ ] 完善邮件解析逻辑
- [ ] 支持多种邮件格式
- [ ] 添加二维码生成
- [ ] 支持批量处理
- [ ] 添加 Web 界面
- [ ] 支持更多票面样式

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## ⚠️ 免责声明

- 本项目仅供学习和技术研究使用
- 生成的车票仅用于展示和收藏，**不具有任何法律效力**
- 请勿将生成的车票用于任何非法目的
- 请遵守相关法律法规

## 📄 许可证

本项目采用 [MIT 许可证](LICENSE) 开源。

## 🙏 致谢

- [Typst](https://typst.app) - 现代排版系统
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) - HTML 解析库
- [12306](https://www.12306.cn) - 中国铁路客户服务中心

---

<p align="center">
  Made with ❤️ for railway enthusiasts
</p>
