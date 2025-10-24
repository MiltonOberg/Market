from flask import Flask

from backend.routes.home import home_bp
from backend.routes.stock_analysis import stock_analysis_bp
from utils.constants import TEMPLATES_DIR


def main():
    app = Flask(__name__, template_folder=TEMPLATES_DIR)
    app.register_blueprint(stock_analysis_bp)
    app.register_blueprint(home_bp)

    app.run(host="127.0.0.1", port=5000, debug=True)


if __name__ == "__main__":
    main()
