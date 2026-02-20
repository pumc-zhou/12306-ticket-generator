// =============================================================================
// 12306 车票 Typst 模板
// =============================================================================
// 
// 本模板用于生成仿真 12306 火车票 PDF
// 
// 使用方法:
//   typst compile ticket.typ output.pdf --input data=ticket_data.json
//
// =============================================================================

// 导入样式定义
#import "styles.typ": *

// 读取车票数据（通过命令行参数传入）
// #let ticket-data = json(sys.inputs.data)

// 临时使用示例数据（开发测试用）
#let ticket-data = (
  passenger_name: "张三",
  id_number: "1101**********1234",
  train_number: "G1234",
  train_date: "2024年01月15日",
  departure_station: "北京南",
  arrival_station: "上海虹桥",
  departure_time: "08:30",
  arrival_time: "12:45",
  coach_number: "05",
  seat_number: "12A",
  seat_class: "二等座",
  ticket_price: 553.0,
  ticket_gate: "B2",
)

// =============================================================================
// 页面设置
// =============================================================================
#set page(
  width: ticket-width,
  height: ticket-height,
  margin: ticket-margin,
)

#set text(
  font: main-font,
  size: base-font-size,
)

// =============================================================================
// 车票主体
// =============================================================================

// 票面背景
#place(
  top + left,
  dx: 0pt,
  dy: 0pt,
  rect(
    width: 100%,
    height: 100%,
    fill: ticket-bg-color,
    stroke: ticket-border,
    radius: ticket-radius,
  )
)

// 左侧色块（车次标识区）
#place(
  top + left,
  dx: 0pt,
  dy: 0pt,
  rect(
    width: 8mm,
    height: 100%,
    fill: accent-color,
    radius: (left: ticket-radius),
  )
)

// -----------------------------------------------------------------------------
// 车票内容区域
// -----------------------------------------------------------------------------
#pad(left: 10mm, top: 4mm, right: 4mm, bottom: 4mm)[
  
  // 第一行：车次号和席别
  #grid(
    columns: (1fr, auto),
    align: (left, right),
    [
      #text(
        size: train-number-size,
        weight: "bold",
        fill: accent-color,
      )[#ticket-data.train_number]
      #h(4mm)
      #text(size: 9pt)[#ticket-data.seat_class]
    ],
    [
      #text(size: 8pt, fill: gray-color)[
        #ticket-data.train_date
      ]
    ]
  )
  
  #v(3mm)
  
  // 第二行：出发站 → 到达站
  #grid(
    columns: (1fr, auto, 1fr),
    align: (left, center, right),
    [
      #text(size: station-font-size, weight: "bold")[
        #ticket-data.departure_station
      ]
      #linebreak()
      #text(size: 10pt, fill: accent-color)[
        #ticket-data.departure_time
      ]
    ],
    [
      #text(size: 14pt, fill: gray-color)[→]
    ],
    [
      #text(size: station-font-size, weight: "bold")[
        #ticket-data.arrival_station
      ]
      #linebreak()
      #text(size: 10pt, fill: gray-color)[
        #ticket-data.arrival_time
      ]
    ]
  )
  
  #v(3mm)
  
  // 分隔线
  #line(length: 100%, stroke: 0.5pt + rgb("#DDDDDD"))
  
  #v(2mm)
  
  // 第三行：乘车人信息和座位信息
  #grid(
    columns: (1fr, 1fr),
    align: (left, right),
    [
      #text(size: 8pt, fill: gray-color)[乘车人]
      #linebreak()
      #text(size: 9pt)[#ticket-data.passenger_name]
      #h(2mm)
      #text(size: 7pt, fill: gray-color)[#ticket-data.id_number]
    ],
    [
      #text(size: 8pt, fill: gray-color)[座位]
      #linebreak()
      #text(size: 9pt)[
        #ticket-data.coach_number 车 #ticket-data.seat_number 号
      ]
    ]
  )
  
  #v(2mm)
  
  // 第四行：票价和检票口
  #grid(
    columns: (1fr, 1fr),
    align: (left, right),
    [
      #text(size: 8pt, fill: gray-color)[票价]
      #linebreak()
      #text(size: 10pt, weight: "bold", fill: price-color)[
        ¥#ticket-data.ticket_price
      ]
    ],
    [
      #text(size: 8pt, fill: gray-color)[检票口]
      #linebreak()
      #text(size: 9pt)[#ticket-data.ticket_gate]
    ]
  )
]

// 右侧二维码区域（占位）
#place(
  top + right,
  dx: -15mm,
  dy: 10mm,
  rect(
    width: 12mm,
    height: 12mm,
    fill: white,
    stroke: 0.5pt + gray-color,
  )
)
