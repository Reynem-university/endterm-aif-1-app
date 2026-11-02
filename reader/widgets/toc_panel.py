"""Оглавление: главы + вложенные заголовки (## / ###)."""
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QLabel, QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget

from ..book import Book
from ..config import TOC_WIDTH
from ..markdown_renderer import Heading


class TocPanel(QWidget):
    chapterRequested = Signal(int, object)  # (индекс главы, якорь | None)

    def __init__(self, book: Book, parent=None):
        super().__init__(parent)
        self.setObjectName("tocPanel")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setFixedWidth(TOC_WIDTH)

        title = QLabel("СОДЕРЖАНИЕ")
        title.setObjectName("tocTitle")

        self.tree = QTreeWidget()
        self.tree.setHeaderHidden(True)
        self.tree.setRootIsDecorated(False)
        self.tree.setIndentation(14)
        self.tree.setWordWrap(True)
        self.tree.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tree.itemClicked.connect(self._on_click)

        lay = QVBoxLayout(self)
        lay.setContentsMargins(0, 0, 0, 8)
        lay.setSpacing(0)
        lay.addWidget(title)
        lay.addWidget(self.tree)

        self._chapter_items: list[QTreeWidgetItem] = []
        for ch in book.chapters:
            item = QTreeWidgetItem(self.tree, [f"{ch.index + 1:02d}   {ch.title}"])
            item.setData(0, Qt.ItemDataRole.UserRole, (ch.index, None))
            self._add_children(item, ch.index, ch.headings)
            self._chapter_items.append(item)

    def _add_children(self, parent: QTreeWidgetItem, chapter: int, headings: list[Heading]):
        for h in headings:
            item = QTreeWidgetItem(parent, [h.title])
            item.setData(0, Qt.ItemDataRole.UserRole, (chapter, h.id))
            self._add_children(item, chapter, h.children)

    def _on_click(self, item: QTreeWidgetItem):
        chapter, anchor = item.data(0, Qt.ItemDataRole.UserRole)
        self.chapterRequested.emit(chapter, anchor)

    def set_current(self, index: int):
        for i, item in enumerate(self._chapter_items):
            item.setExpanded(i == index)
        if 0 <= index < len(self._chapter_items):
            self.tree.setCurrentItem(self._chapter_items[index])
