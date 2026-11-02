"""Главное окно: связывает книгу, оглавление, навигацию, прогресс и полноэкранный режим."""
from pathlib import Path

from PySide6.QtCore import QSettings, QUrl
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtWidgets import QHBoxLayout, QMainWindow, QProgressBar, QVBoxLayout, QWidget

from .book import build_page, empty_page, load_book
from .config import APP_NAME, APP_ORG, ZOOM_DEFAULT, ZOOM_MAX, ZOOM_MIN, ZOOM_STEP
from .theme import APP_QSS
from .widgets.bars import FooterBar, TopBar
from .widgets.reader_view import ReaderView
from .widgets.toc_panel import TocPanel


class MainWindow(QMainWindow):
    def __init__(self, content_dir: Path):
        super().__init__()
        self.book = load_book(content_dir)
        self.base_url = QUrl.fromLocalFile(str(content_dir.resolve()) + "/")
        self.settings = QSettings(APP_ORG, APP_NAME)

        self.index = 0
        self.chapter_frac = 0.0
        self.zoom = float(self.settings.value("zoom", ZOOM_DEFAULT))
        self._toc_wanted = True

        self.setWindowTitle(f"{self.book.title} — {APP_NAME}")
        self.setMinimumSize(1000, 680)
        self.setStyleSheet(APP_QSS)
        self._build_ui()
        self._bind_keys()

        geo = self.settings.value("geometry")
        if geo:
            self.restoreGeometry(geo)
        else:
            self.resize(1280, 820)

        self.view.change_zoom(self.zoom)
        if self.book.chapters:
            self.open_chapter(int(self.settings.value("chapter", 0)),
                              fraction=float(self.settings.value("fraction", 0.0)))
        else:
            self.view.show_html(empty_page(), self.base_url)

    # ---- UI --------------------------------------------------------------- #
    def _build_ui(self):
        self.topbar = TopBar(self.book.title, self.book.subtitle)
        self.progress = QProgressBar()
        self.progress.setRange(0, 1000)
        self.progress.setTextVisible(False)
        self.toc = TocPanel(self.book)
        self.view = ReaderView()
        self.footer = FooterBar()

        body = QHBoxLayout()
        body.setContentsMargins(0, 0, 0, 0)
        body.setSpacing(0)
        body.addWidget(self.toc)
        body.addWidget(self.view, 1)

        root = QWidget(); root.setObjectName("root")
        lay = QVBoxLayout(root)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(0)
        lay.addWidget(self.topbar)
        lay.addWidget(self.progress)
        lay.addLayout(body, 1)
        lay.addWidget(self.footer)
        self.setCentralWidget(root)

        self.topbar.tocToggled.connect(self.toggle_toc)
        self.topbar.prevClicked.connect(self.prev_chapter)
        self.topbar.nextClicked.connect(self.next_chapter)
        self.topbar.zoomIn.connect(lambda: self.set_zoom(self.zoom + ZOOM_STEP))
        self.topbar.zoomOut.connect(lambda: self.set_zoom(self.zoom - ZOOM_STEP))
        self.topbar.fullscreenClicked.connect(self.toggle_fullscreen)
        self.toc.chapterRequested.connect(self._on_toc_request)
        self.view.progressChanged.connect(self._on_progress)

    def _bind_keys(self):
        binds = {
            "Right": self.next_chapter, "Alt+Right": self.next_chapter,
            "Left": self.prev_chapter, "Alt+Left": self.prev_chapter,
            "F11": self.toggle_fullscreen, "F": self.toggle_fullscreen,
            "Ctrl+T": self.toggle_toc,
            "Ctrl+=": lambda: self.set_zoom(self.zoom + ZOOM_STEP),
            "Ctrl++": lambda: self.set_zoom(self.zoom + ZOOM_STEP),
            "Ctrl+-": lambda: self.set_zoom(self.zoom - ZOOM_STEP),
            "Ctrl+0": lambda: self.set_zoom(ZOOM_DEFAULT),
            "Esc": self._exit_fullscreen,
        }
        for seq, slot in binds.items():
            act = QAction(self)
            act.setShortcut(QKeySequence(seq))
            act.triggered.connect(slot)
            self.addAction(act)

    # ---- навигация -------------------------------------------------------- #
    def open_chapter(self, index: int, anchor: str | None = None, fraction: float = 0.0):
        total = len(self.book.chapters)
        if not total:
            return
        self.index = max(0, min(index, total - 1))
        chapter = self.book.chapters[self.index]
        self.view.show_html(build_page(self.book, chapter), self.base_url, anchor, fraction)
        self.toc.set_current(self.index)
        self.footer.set_chapter(self.index + 1, total, chapter.title)
        self.topbar.set_nav_enabled(self.index > 0, self.index < total - 1)

    def next_chapter(self):
        if self.index < len(self.book.chapters) - 1:
            self.open_chapter(self.index + 1)

    def prev_chapter(self):
        if self.index > 0:
            self.open_chapter(self.index - 1)

    def _on_toc_request(self, index: int, anchor):
        if index != self.index:
            self.open_chapter(index, anchor)
        elif anchor:
            self.view.scroll_to(anchor)
        else:
            self.view.scroll_top()

    # ---- прогресс --------------------------------------------------------- #
    def _on_progress(self, frac: float):
        self.chapter_frac = frac
        total = max(len(self.book.chapters), 1)
        overall = (self.index + frac) / total
        self.progress.setValue(int(overall * 1000))
        self.footer.set_progress(frac, overall)

    # ---- режимы ----------------------------------------------------------- #
    def toggle_toc(self):
        visible = not self.toc.isVisible()
        self.toc.setVisible(visible)
        if not self.isFullScreen():
            self._toc_wanted = visible

    def set_zoom(self, value: float):
        self.zoom = round(max(ZOOM_MIN, min(ZOOM_MAX, value)), 2)
        self.view.change_zoom(self.zoom)

    def toggle_fullscreen(self):
        if self.isFullScreen():
            self._exit_fullscreen()
        else:
            self.showFullScreen()
            self.topbar.hide()      # режим фокуса: только текст, прогресс и статус
            self.toc.hide()         # Ctrl+T вернёт оглавление

    def _exit_fullscreen(self):
        if self.isFullScreen():
            self.showNormal()
            self.topbar.show()
            self.toc.setVisible(self._toc_wanted)

    # ---- сохранение состояния -------------------------------------------- #
    def closeEvent(self, event):
        self.settings.setValue("geometry", self.saveGeometry())
        self.settings.setValue("chapter", self.index)
        self.settings.setValue("fraction", self.chapter_frac)
        self.settings.setValue("zoom", self.zoom)
        super().closeEvent(event)
