"""Загрузка книги: content/book.json + content/chapters/*.md (порядок по имени файла)."""
import json
import re
from dataclasses import dataclass, field
from html import escape
from pathlib import Path

from .markdown_renderer import Heading, render
from .theme import PAGE_CSS


@dataclass
class Chapter:
    index: int
    path: Path
    title: str
    body: str
    headings: list[Heading] = field(default_factory=list)


@dataclass
class Book:
    root: Path
    title: str
    subtitle: str
    authors: list[str]
    chapters: list[Chapter]


def load_book(root: Path) -> Book:
    meta_file = root / "book.json"
    meta = json.loads(meta_file.read_text("utf-8")) if meta_file.exists() else {}

    chapters: list[Chapter] = []
    for i, path in enumerate(sorted((root / "chapters").glob("*.md"))):
        text = path.read_text("utf-8")
        m = re.search(r"^#\s+(.+?)\s*$", text, re.M)
        body, headings = render(text)
        chapters.append(Chapter(i, path, m.group(1) if m else path.stem, body, headings))

    return Book(
        root=root,
        title=meta.get("title", "Без названия"),
        subtitle=meta.get("subtitle", ""),
        authors=meta.get("authors", []),
        chapters=chapters,
    )


def build_page(book: Book, chapter: Chapter) -> str:
    n, total = chapter.index + 1, len(book.chapters)
    return f"""<!doctype html><html lang="ru"><head><meta charset="utf-8">
<style>{PAGE_CSS}</style></head><body><main class="sheet">
<div class="eyebrow"><span>CH {n:02d}</span><span class="sep"></span><span class="total">{total:02d}</span></div>
<article>{chapter.body}</article>
<div class="end">{escape(book.title)} · {n:02d}/{total:02d}</div>
</main></body></html>"""


def empty_page() -> str:
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{PAGE_CSS}</style></head>"
            "<body><main class='sheet'><article><h1>Нет глав</h1>"
            "<p>Добавьте файлы <code>content/chapters/*.md</code>.</p></article></main></body></html>")
