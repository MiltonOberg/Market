from subprocess import run
from utils.constants import FRONTEND_DIR


def run_dashboard():
    run(["streamlit", "run", FRONTEND_DIR / "dashboard.py"])


if __name__ == "__main__":
    run_dashboard()
