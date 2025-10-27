from flask import Flask

from backend.routes.ai_model_route import ai_model_bp
from backend.routes.home_route import home_bp
from backend.routes.stock_analysis_route import stock_analysis_bp
from utils.constants import STATIC_DIR, TEMPLATES_DIR


def main():
    app = Flask(__name__, template_folder=TEMPLATES_DIR, static_folder=STATIC_DIR)
    app.register_blueprint(home_bp)
    app.register_blueprint(stock_analysis_bp)
    app.register_blueprint(ai_model_bp)

    app.run(host="127.0.0.1", port=5000, debug=True)


if __name__ == "__main__":
    main()
