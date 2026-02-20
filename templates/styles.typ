// styles.typ — 颜色、间距及字体样式定义
//
// 本文件集中管理票面的视觉规范，供 ticket.typ 导入使用。

// ──────────────────────────────
// 颜色
// ──────────────────────────────
#let ticket-colors = (
  primary:    rgb("#C0392B"),   // 主色：中国红
  secondary:  rgb("#2C3E50"),   // 辅色：深蓝灰（文字）
  accent:     rgb("#E74C3C"),   // 强调色
  background: rgb("#FDFAF6"),   // 票面底色：米白
  border:     rgb("#BDC3C7"),   // 边框色
  muted:      rgb("#7F8C8D"),   // 次要文字
)

// ──────────────────────────────
// 字体
// ──────────────────────────────
#let ticket-fonts = (
  // 中文优先使用思源黑体，回退到其他 CJK 字体
  sans: ("Source Han Sans SC", "Noto Sans CJK SC", "PingFang SC", "Microsoft YaHei", "Arial"),
  // 数字/英文使用等宽字体，方便对齐车次、座位号等信息
  mono: ("JetBrains Mono", "Courier New", "monospace"),
)

// ──────────────────────────────
// 间距
// ──────────────────────────────
#let ticket-spacing = (
  xs:  2mm,
  sm:  4mm,
  md:  6mm,
  lg:  10mm,
  xl:  16mm,
)
