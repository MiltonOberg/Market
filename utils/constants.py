from pathlib import Path

FRONTEND_DIR = Path(__file__).parents[1] / "frontend"
TEMPLATES_DIR = FRONTEND_DIR / "templates"
STATIC_DIR = FRONTEND_DIR / "static"


if __name__ == "__main__":
    print(FRONTEND_DIR)
