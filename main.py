import portfolio


def main():
    pf = portfolio.Portfolio("weights.json")
    pf.holdings_history("holdings.xlsx")


if __name__ == "__main__":
    main()
