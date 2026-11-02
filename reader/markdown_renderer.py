"""Markdown -> HTML + дерево заголовков для оглавления."""
import html
import re
from dataclasses import dataclass, field

import markdown

_EXTENSIONS = ["extra", "admonition", "toc", "sane_lists"]
_CONFIG = {}

try:  # подсветка кода, если установлен Pygments
    import pygments  # noqa: F401
    _EXTENSIONS.append("codehilite")
    _CONFIG["codehilite"] = {"guess_lang": False, "css_class": "codehilite"}
except ImportError:
    pass


def _slug(value: str, sep: str) -> str:
    """Slug с поддержкой кириллицы."""
    value = re.sub(r"[^\w\s-]", "", value, flags=re.UNICODE).strip().lower()
    return re.sub(r"[\s_-]+", sep, value)


_CONFIG["toc"] = {"toc_depth": "2-3", "slugify": _slug}

# <p><img alt="Подпись" ...></p>  ->  <figure><img><figcaption>Подпись</figcaption></figure>
_FIGURE = re.compile(r'<p>\s*(<img\b[^>]*?alt="([^"]*)"[^>]*>)\s*</p>')


def _to_figure(m: re.Match) -> str:
    img, caption = m.group(1), m.group(2).strip()
    cap = f"<figcaption>{caption}</figcaption>" if caption else ""
    return f"<figure>{img}{cap}</figure>"


@dataclass
class Heading:
    id: str
    title: str
    level: int
    children: list["Heading"] = field(default_factory=list)


def _build(tokens: list[dict]) -> list[Heading]:
    result = []
    for t in tokens:
        title = html.unescape(re.sub(r"<[^>]+>", "", t["name"]))
        result.append(Heading(t["id"], title, t["level"], _build(t.get("children", []))))
    return result


def render(text: str) -> tuple[str, list[Heading]]:
    md = markdown.Markdown(extensions=_EXTENSIONS, extension_configs=_CONFIG)
    body = _FIGURE.sub(_to_figure, md.convert(text))
    return body, _build(md.toc_tokens)
