"""Светлая hi-tech тема: палитра, QSS для Qt-виджетов и CSS страницы книги."""
from string import Template

try:
    from pygments.formatters import HtmlFormatter
    _CODE_CSS = HtmlFormatter(style="friendly").get_style_defs(".codehilite")
except ImportError:  # подсветка кода опциональна
    _CODE_CSS = ""

PALETTE = {
    "bg": "#F4F6FA",
    "surface": "#FFFFFF",
    "ink": "#0F172A",
    "text": "#1E293B",
    "muted": "#64748B",
    "line": "#E2E8F0",
    "accent": "#0066FF",
    "accent2": "#00C2D1",
    "accent_soft": "#E8F1FF",
    "code_bg": "#F1F5F9",
    "sans": '"Inter","Segoe UI","SF Pro Text","Helvetica Neue",Arial,sans-serif',
    "mono": '"JetBrains Mono","Cascadia Mono","SF Mono",Consolas,"Courier New",monospace',
}

# --------------------------------------------------------------------------- #
# QSS (интерфейс вокруг текста)
# --------------------------------------------------------------------------- #
APP_QSS = Template("""
QMainWindow, #root { background: $bg; }
QLabel { color: $text; font-family: $sans; }

#topbar, #footer { background: $surface; }
#topbar { border-bottom: 1px solid $line; }
#footer { border-top: 1px solid $line; }

#brand   { font-family: $mono; font-size: 12px; font-weight: 700; color: $ink; }
#subbrand{ font-family: $mono; font-size: 11px; color: $muted; }
#meta    { font-family: $mono; font-size: 11px; color: $muted; }
#metaAcc { font-family: $mono; font-size: 11px; color: $accent; font-weight: 700; }

QPushButton#ghost {
    background: transparent; color: #334155;
    border: 1px solid $line; border-radius: 6px;
    padding: 6px 12px; font-family: $mono; font-size: 11px;
}
QPushButton#ghost:hover   { border-color: $accent; color: $accent; background: $accent_soft; }
QPushButton#ghost:pressed { background: #D6E6FF; }
QPushButton#ghost:disabled{ color: #CBD5E1; border-color: #EEF2F7; background: transparent; }

QProgressBar { border: none; background: $line; min-height: 3px; max-height: 3px; }
QProgressBar::chunk {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 $accent, stop:1 $accent2);
}

#tocPanel { background: $surface; border-right: 1px solid $line; }
#tocTitle { font-family: $mono; font-size: 11px; color: $muted; padding: 18px 20px 8px 20px; }
QTreeWidget {
    background: transparent; border: none; outline: 0;
    font-family: $sans; font-size: 13px; color: $text;
}
QTreeWidget::item { padding: 7px 8px; margin: 1px 10px; border-radius: 6px; }
QTreeWidget::item:hover    { background: #F1F6FF; }
QTreeWidget::item:selected { background: $accent_soft; color: $accent; }
QTreeWidget::branch { image: none; border-image: none; }

QScrollBar:vertical { background: transparent; width: 8px; margin: 2px; }
QScrollBar::handle:vertical { background: #CBD5E1; border-radius: 3px; min-height: 30px; }
QScrollBar::handle:vertical:hover { background: #94A3B8; }
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { height: 0; }
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical { background: transparent; }
""").substitute(PALETTE)

# --------------------------------------------------------------------------- #
# CSS страницы (внутри QWebEngineView)
# --------------------------------------------------------------------------- #
PAGE_CSS = Template("""
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
    margin: 0; padding: 48px 24px 80px;
    background-color: $bg;
    background-image: radial-gradient(#D9E0EC 1px, transparent 1px);
    background-size: 24px 24px;
    color: $text; font-family: $sans; font-size: 17px; line-height: 1.75;
    -webkit-font-smoothing: antialiased;
}
.sheet { max-width: 800px; margin: 0 auto; }
.eyebrow {
    display: flex; align-items: center; gap: 12px; margin-bottom: 14px;
    font-family: $mono; font-size: 12px; color: $accent; font-weight: 700;
}
.eyebrow .sep { flex: 1; height: 1px; background: linear-gradient(90deg, $accent, transparent); }
.eyebrow .total { color: $muted; font-weight: 400; }

article {
    position: relative; background: $surface; border: 1px solid $line;
    border-radius: 14px; padding: 56px 64px;
    box-shadow: 0 1px 2px rgba(15,23,42,.04), 0 12px 32px rgba(15,23,42,.05);
}
article::before {
    content: ""; position: absolute; left: 0; right: 0; top: 0; height: 3px;
    border-radius: 14px 14px 0 0;
    background: linear-gradient(90deg, $accent, $accent2);
}

h1, h2, h3, h4 { color: $ink; line-height: 1.25; letter-spacing: -0.015em; }
h1 { font-size: 2.3em; font-weight: 750; margin: 0 0 .8em; }
h1::after {
    content: ""; display: block; width: 64px; height: 4px; margin-top: .45em;
    background: linear-gradient(90deg, $accent, $accent2); border-radius: 2px;
}
h2 { font-size: 1.5em; margin: 2.2em 0 .7em; font-weight: 700; }
h2::before {
    content: ""; display: inline-block; width: 10px; height: 10px; margin-right: 12px;
    background: $accent; border-radius: 2px; transform: translateY(-2px);
}
h3 { font-size: 1.2em; margin: 1.8em 0 .5em; font-weight: 650; }
p { margin: 0 0 1.1em; }
a { color: $accent; text-decoration: none; border-bottom: 1px solid rgba(0,102,255,.3); }
a:hover { border-bottom-color: $accent; }
strong { color: $ink; }
hr { border: none; height: 1px; background: $line; margin: 2.4em 0; }

ul, ol { padding-left: 1.4em; margin: 0 0 1.1em; }
li { margin: .3em 0; }
li::marker { color: $accent; }

blockquote {
    margin: 1.6em 0; padding: .6em 1.2em; color: #334155;
    border-left: 3px solid $accent; background: $accent_soft; border-radius: 0 8px 8px 0;
}
blockquote p:last-child { margin: 0; }

code {
    font-family: $mono; font-size: .86em; background: $code_bg;
    border: 1px solid $line; border-radius: 5px; padding: .1em .4em;
}
pre {
    background: $code_bg; border: 1px solid $line; border-radius: 10px;
    padding: 16px 20px; overflow-x: auto; line-height: 1.55; margin: 1.4em 0;
}
pre code { background: none; border: none; padding: 0; font-size: .85em; }
.codehilite { background: transparent !important; }

table { border-collapse: collapse; width: 100%; margin: 1.6em 0; font-size: .95em; }
th {
    text-align: left; font-family: $mono; font-size: .78em; text-transform: uppercase;
    color: $muted; border-bottom: 2px solid $accent; padding: 10px 12px;
}
td { padding: 10px 12px; border-bottom: 1px solid $line; }
tr:hover td { background: #F8FAFD; }

figure { margin: 2em 0; text-align: center; }
img { max-width: 100%; height: auto; border-radius: 10px; border: 1px solid $line; }
figcaption {
    margin-top: .8em; font-family: $mono; font-size: 12px; color: $muted;
}
figcaption::before { content: "FIG. "; color: $accent; font-weight: 700; }

.admonition {
    margin: 1.6em 0; padding: 14px 20px; border: 1px solid #CFE0FF;
    border-left: 4px solid $accent; background: $accent_soft; border-radius: 8px;
}
.admonition-title {
    font-family: $mono; font-size: 12px; text-transform: uppercase;
    font-weight: 700; color: $accent; margin: 0 0 .4em; letter-spacing: .06em;
}
.admonition p:last-child { margin-bottom: 0; }
.admonition.warning { background: #FFF7E6; border-color: #FFE0A3; border-left-color: #F59E0B; }
.admonition.warning .admonition-title { color: #B45309; }
.admonition.danger  { background: #FEECEC; border-color: #FBC7C7; border-left-color: #EF4444; }
.admonition.danger .admonition-title  { color: #B91C1C; }

.end {
    margin-top: 28px; text-align: center; font-family: $mono;
    font-size: 11px; color: $muted;
}
::-webkit-scrollbar { width: 10px; }
::-webkit-scrollbar-thumb { background: #CBD5E1; border-radius: 5px; border: 2px solid $bg; }
""").substitute(PALETTE) + _CODE_CSS
