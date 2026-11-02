"""Верхняя панель управления и нижняя строка состояния."""
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QPushButton


def _button(text: str, tip: str) -> QPushButton:
    b = QPushButton(text)
    b.setObjectName("ghost")
    b.setToolTip(tip)
    b.setCursor(Qt.CursorShape.PointingHandCursor)
    b.setFocusPolicy(Qt.FocusPolicy.NoFocus)
    return b


class TopBar(QFrame):
    tocToggled = Signal()
    prevClicked = Signal()
    nextClicked = Signal()
    zoomIn = Signal()
    zoomOut = Signal()
    fullscreenClicked = Signal()

    def __init__(self, title: str, subtitle: str, parent=None):
        super().__init__(parent)
        self.setObjectName("topbar")
        self.setFixedHeight(52)

        self.toc_btn = _button("☰ TOC", "Оглавление (Ctrl+T)")
        self.prev_btn = _button("◂ PREV", "Предыдущая глава (←)")
        self.next_btn = _button("NEXT ▸", "Следующая глава (→)")
        zout = _button("A−", "Уменьшить шрифт (Ctrl+−)")
        zin = _button("A+", "Увеличить шрифт (Ctrl+=)")
        full = _button("⤢ FULL", "Полный экран (F11)")

        brand = QLabel(title.upper()); brand.setObjectName("brand")
        sub = QLabel(f"// {subtitle.upper()}" if subtitle else ""); sub.setObjectName("subbrand")

        lay = QHBoxLayout(self)
        lay.setContentsMargins(16, 0, 16, 0)
        lay.setSpacing(8)
        for w in (self.toc_btn, brand, sub):
            lay.addWidget(w)
        lay.addStretch(1)
        for w in (zout, zin, self.prev_btn, self.next_btn, full):
            lay.addWidget(w)

        self.toc_btn.clicked.connect(self.tocToggled)
        self.prev_btn.clicked.connect(self.prevClicked)
        self.next_btn.clicked.connect(self.nextClicked)
        zout.clicked.connect(self.zoomOut)
        zin.clicked.connect(self.zoomIn)
        full.clicked.connect(self.fullscreenClicked)

    def set_nav_enabled(self, has_prev: bool, has_next: bool):
        self.prev_btn.setEnabled(has_prev)
        self.next_btn.setEnabled(has_next)


class FooterBar(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("footer")
        self.setFixedHeight(32)

        self.chapter_lbl = QLabel(); self.chapter_lbl.setObjectName("meta")
        self.chapter_pct = QLabel(); self.chapter_pct.setObjectName("meta")
        self.total_pct = QLabel(); self.total_pct.setObjectName("metaAcc")

        lay = QHBoxLayout(self)
        lay.setContentsMargins(16, 0, 16, 0)
        lay.setSpacing(18)
        lay.addWidget(self.chapter_lbl)
        lay.addStretch(1)
        lay.addWidget(self.chapter_pct)
        lay.addWidget(self.total_pct)

    def set_chapter(self, number: int, total: int, title: str):
        self.chapter_lbl.setText(f"CH {number:02d}/{total:02d}  ·  {title}")

    def set_progress(self, chapter_frac: float, total_frac: float):
        self.chapter_pct.setText(f"CHAPTER {chapter_frac * 100:3.0f}%")
        self.total_pct.setText(f"TOTAL {total_frac * 100:3.0f}%")
