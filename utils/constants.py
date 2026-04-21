from pathlib import Path

FRONTEND_DIR = Path(__file__).parents[1] / "frontend"
TEMPLATES_DIR = FRONTEND_DIR / "templates"
STATIC_DIR = FRONTEND_DIR / "static"
FEATURES_DIR = Path(__file__).parents[1] / "backend" / "features"
MODELS_DIR = FEATURES_DIR / "models"
WEIGHTS_DIR = MODELS_DIR / "weights"
MULTI_WEIGHTS_DIR = WEIGHTS_DIR / "multi_agent.keras"


if __name__ == "__main__":
    print(WEIGHTS_DIR)
