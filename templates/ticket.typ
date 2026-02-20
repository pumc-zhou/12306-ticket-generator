// ticket.typ — 核心排版逻辑
//
// 本文件定义 12306 车票的整体版面结构。
// 通过 `--input data=<JSON>` 将票务数据从外部注入。
//
// 依赖：
//   #import "styles.typ": *

#import "styles.typ": ticket-colors, ticket-fonts, ticket-spacing

// 从命令行 --input 读取 JSON 数据（实际渲染时由 renderer.py 传入）
// 示例结构：
// {
//   "passenger": "张三",
//   "train_no": "G1234",
//   "departure": "北京南",
//   "destination": "上海虹桥",
//   "departure_time": "2026-01-01 08:00",
//   "seat_type": "二等座",
//   "seat_no": "05车08D号",
//   "ticket_type": "成人票",
//   "price": "553.0元",
//   "order_no": "E123456789"
// }

// TODO: 使用 sys.inputs 读取并反序列化 JSON，完成完整排版实现。

#set page(
  width: 210mm,
  height: 99mm,
  margin: (x: 8mm, y: 6mm),
)

#set text(
  font: ("Source Han Sans SC", "Noto Sans CJK SC", "Arial"),
  size: 10pt,
)

// 占位内容 — 待实现完整排版逻辑后替换
#align(center)[
  #text(size: 16pt, weight: "bold")[中国铁路 12306 电子客票]
  #v(4mm)
  #text(size: 10pt, fill: gray)[模板占位符 — 请在 ticket.typ 中完成完整排版]
]
