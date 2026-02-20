# 12306-ticket-generator

> 从 12306 购票成功通知邮件自动生成仿真 PDF 电子客票。  
> 使用 **Python** 解析邮件 HTML，使用 **[Typst](https://typst.app/)** 进行高质量排版输出。

---

## 目录结构

```
12306-ticket-generator/
├── assets/               # 静态资源
│   ├── fonts/            # 自定义字体（如思源黑体、方正等）
│   └── backgrounds/      # 票面底纹背景图 (SVG/PNG)
├── src/                  # 核心代码
│   ├── parser/           # 邮件解析模块 (Python)
│   │   └── parser.py     # 从 12306 邮件 HTML 中提取结构化票务信息
│   └── renderer/         # Typst 调用封装
│       └── renderer.py   # 将票务数据注入 Typst 模板并编译为 PDF
├── templates/            # Typst 模板文件
│   ├── ticket.typ        # 核心排版逻辑（票面整体版面）
│   └── styles.typ        # 颜色、间距、字体等样式定义
├── tests/                # 测试用例
│   └── emails/           # 存放 12306 邮件的 HTML 源码示例
├── output/               # 生成的 PDF 存放处（自动创建）
├── requirements.txt      # Python 依赖
└── main.py               # 项目入口
```

---

## 快速开始

### 环境依赖

| 依赖 | 版本要求 | 说明 |
|------|---------|------|
| Python | ≥ 3.10 | 核心运行环境 |
| [Typst](https://github.com/typst/typst/releases) | ≥ 0.11 | PDF 排版引擎，需加入 `PATH` |

### 安装

```bash
# 1. 克隆项目
git clone https://github.com/pumc-zhou/12306-ticket-generator.git
cd 12306-ticket-generator

# 2. 安装 Python 依赖
pip install -r requirements.txt

# 3. 安装 Typst（以 macOS 为例）
brew install typst
# 或参考 https://github.com/typst/typst#installation 选择对应平台安装方式
```

### 使用方法

```bash
python main.py --email tests/emails/sample.html --output my_ticket.pdf
```

生成的 PDF 文件会保存在 `output/` 目录下。

---

## 模块说明

### `src/parser/parser.py` — 邮件解析模块

负责从 12306 发送的购票成功通知邮件（HTML 格式）中提取结构化票务信息。

- `parse_email(html_source: str) -> list[TicketInfo]`：从 HTML 字符串解析票务数据。
- `parse_email_file(path) -> list[TicketInfo]`：从本地 HTML 文件解析票务数据。
- `TicketInfo`：数据类，包含乘客姓名、车次、出发 / 到达站、座位等字段。

### `src/renderer/renderer.py` — Typst 渲染封装

将解析后的票务数据序列化为 JSON，通过 Typst CLI 的 `--input` 参数注入模板，编译生成 PDF。

- `render_ticket(ticket_data: dict, output_filename: str) -> Path`：渲染单张车票并返回输出路径。

### `templates/ticket.typ` — 核心排版模板

定义票面整体版面：票号区、乘客信息区、行程信息区、二维码区等。

### `templates/styles.typ` — 样式定义

集中管理票面的视觉规范：
- `ticket-colors`：主色（中国红）、辅色、背景色等。
- `ticket-fonts`：中文（思源黑体优先）、等宽字体配置。
- `ticket-spacing`：统一间距常量（xs / sm / md / lg / xl）。

### `assets/fonts/`

存放项目使用的自定义字体文件（`.ttf` / `.otf`）。推荐使用：
- **[思源黑体 (Source Han Sans SC)](https://github.com/adobe-fonts/source-han-sans)**
- **[方正字体](https://www.foundertype.com/)**

### `assets/backgrounds/`

存放票面底纹背景图，支持 SVG / PNG 格式。

### `tests/emails/`

存放用于测试的 12306 邮件 HTML 源码示例文件。将购票成功通知邮件的 HTML 源码保存于此，供解析模块使用。

---

## 开发计划

- [ ] 实现 `parser.py` 的完整 HTML 解析逻辑
- [ ] 实现 `renderer.py` 的完整 Typst 调用逻辑
- [ ] 完成 `ticket.typ` 票面排版设计
- [ ] 添加字体和背景图资源
- [ ] 编写单元测试

---

## 许可证

本项目基于 [LICENSE](LICENSE) 协议开源。