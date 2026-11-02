"""Область чтения: QWebEngineView + прогресс прокрутки."""
import json

from PySide6.QtCore import QUrl, Signal
from PySide6.QtGui import QColor, QDesktopServices
from PySide6.QtWebEngineCore import QWebEnginePage
from PySide6.QtWebEngineWidgets import QWebEngineView


class _Page(QWebEnginePage):
    """Внешние ссылки открываем в браузере, остальное — внутри."""

    def acceptNavigationRequest(self, url, nav_type, is_main_frame):
        if nav_type == QWebEnginePage.NavigationType.NavigationTypeLinkClicked:
            if url.scheme() in ("http", "https", "mailto"):
                QDesktopServices.openUrl(url)
                return False
        return super().acceptNavigationRequest(url, nav_type, is_main_frame)


class ReaderView(QWebEngineView):
    progressChanged = Signal(float)  # доля прокрутки текущей главы, 0..1

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setPage(_Page(self))
        self.page().setBackgroundColor(QColor("#F4F6FA"))
        self._anchor: str | None = None
        self._fraction = 0.0
        self.page().scrollPositionChanged.connect(self._emit_progress)
        self.page().contentsSizeChanged.connect(self._emit_progress)
        self.loadFinished.connect(self._on_loaded)

    # ---- публичный API ---------------------------------------------------- #
    def show_html(self, html: str, base_url: QUrl, anchor: str | None = None,
                  fraction: float = 0.0) -> None:
        self._anchor, self._fraction = anchor, fraction
        self.setHtml(html, base_url)  # лимит setHtml ~2 МБ; картинки грузятся по file://

    def scroll_to(self, anchor: str) -> None:
        js = (f"document.getElementById({json.dumps(anchor)})"
              "?.scrollIntoView({behavior:'smooth',block:'start'});")
        self.page().runJavaScript(js)

    def scroll_top(self) -> None:
        self.page().runJavaScript("window.scrollTo({top:0,behavior:'smooth'});")

    def change_zoom(self, value: float) -> None:
        self.setZoomFactor(value)

    # ---- внутреннее ------------------------------------------------------- #
    def _on_loaded(self, ok: bool) -> None:
        if ok and self._anchor:
            self.scroll_to(self._anchor)
        elif ok and self._fraction > 0:
            self.page().runJavaScript(
                f"window.scrollTo({{top:{self._fraction}*(document.documentElement.scrollHeight"
                "-window.innerHeight),behavior:'instant'});")
        self._emit_progress()

    def _emit_progress(self, *_):
        total = self.page().contentsSize().height()
        span = total - self.height() / max(self.zoomFactor(), 0.1)
        if span <= 1:
            self.progressChanged.emit(1.0)
            return
        y = self.page().scrollPosition().y()
        self.progressChanged.emit(min(max(y / span, 0.0), 1.0))
