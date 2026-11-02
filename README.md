# AI Reader

Электронная читалка на PySide6 (Qt WebEngine). Светлая hi-tech тема.

## Запуск
    pip install -r requirements.txt
    python main.py

## Структура
    main.py                      точка входа
    reader/app.py                главное окно, навигация, прогресс, fullscreen
    reader/book.py               загрузка глав, сборка HTML-страницы
    reader/markdown_renderer.py  Markdown -> HTML + дерево заголовков
    reader/theme.py              палитра, QSS и CSS страницы (весь стиль здесь)
    reader/widgets/              TopBar/FooterBar, TocPanel, ReaderView
    content/book.json            название, подзаголовок, авторы
    content/chapters/*.md        главы (порядок по имени файла: 01_, 02_ ...)
    content/assets/              картинки

## Как добавить контент
Новая глава = новый файл `content/chapters/NN_name.md`, первая строка `# Название`.
Картинки кладём в `content/assets/` и вставляем: `![Подпись](assets/file.png)`
(путь считается от папки `content/`). Ширина: `![Подпись](assets/file.png){ width=60% }`.
Врезки: `!!! note "Заголовок"` + текст с отступом в 4 пробела (note / warning / danger).

## Управление
← / → — глава, F11 или F — полный экран, Esc — выход, Ctrl+T — оглавление,
Ctrl +/−/0 — размер шрифта. Позиция чтения и масштаб сохраняются.
