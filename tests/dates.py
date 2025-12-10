from backend.components.stock import Stock

if __name__ == "__main__":
    stock = Stock("saab")
    print(stock.df.index.strftime("%y-%m-%d"))
