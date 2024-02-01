from dataclasses import dataclass
import pandas as pd
import yfinance as yf
import json


@dataclass
class Position:
    quantity: int = 0  # + long, - short
    symbol: str = ""
    weight: float = 0.0


class Portfolio:
    holdings: [Position]

    def __init__(self, fname: str):
        self.holdings = []
        with open(fname, "r") as f:
            data = json.load(f)
            holdings = data["holdings"]
            for d in holdings:
                print(d)
                self.holdings.append(Position(**d))

    def holdings_history(self, path: str):
        with pd.ExcelWriter(path, engine="xlsxwriter") as writer:
            for index, holding in enumerate(self.holdings, start=1):
                ticker = yf.Ticker(holding.symbol)
                history = ticker.history(period="5y", interval="1mo")
                history.index = history.index.tz_localize(None)
                history.to_excel(writer, sheet_name=f"{holding.symbol}")
