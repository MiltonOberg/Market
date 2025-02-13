class Stonk:
    def __init__(self, stonk, market_value: str, profit: int, pe: float):
        self.stonk = stonk
        self.pe = pe
        self.market_value = self._get_market_value_b(market_value)
        self.profit = self._get_profit_b(profit)
        self._profit_value = self._get_profit_value()

    @property
    def profit_value(
        self,
    ):
        return f"{self._profit_value:,}".replace(",", " ")

    @property
    def profit_market_eval(self):
        return f"""
    {self.stonk} värderat på vinster: {self.profit_value}
    Börsvärde: {self.market_value}
    Visas i miljarder
    """

    def _get_market_value_b(self, value: str) -> float:
        numbers = value.split(",")[0].replace(" ", "")
        return float(numbers) / 1000

    def _get_profit_b(self, value: int) -> float:
        return float(value) / 1000

    def _get_profit_value(self):
        return int(self.profit * self.pe)
