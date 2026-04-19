from backend.components.stock import Stock
from backend.features.models.multi_agent import MultiAgent
from utils.stock_list import SWEDISH_STOCKS


def screen_stocks():
    # results = []

    for ticker in SWEDISH_STOCKS:
        stock = Stock(stock=ticker)
        agent = MultiAgent(stock)
        agent.train()
