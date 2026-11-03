from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
ICON_PATH = ROOT_DIR / "content" / "favicon.ico"

"""Константы приложения."""
APP_NAME = "AI Reader"
APP_ORG = "AIReader"

ZOOM_MIN, ZOOM_MAX, ZOOM_STEP, ZOOM_DEFAULT = 0.7, 1.8, 0.1, 1.0
TOC_WIDTH = 300
