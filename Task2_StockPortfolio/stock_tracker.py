stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 130,
    "MSFT": 320
}

def track_portfolio():
    portfolio = {}   
    total_investment = 0

    print("Available stocks:", ", ".join(stock_prices.keys()))
    print("Type 'done' when you finish entering stocks.\n")

    while True:
        stock = input("Enter stock symbol (or 'done'): ").upper()

        if stock == "DONE":
            break

        if stock not in stock_prices:
            print("Stock not found in our price list. Try again.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock}: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        cost = stock_prices[stock] * quantity
        portfolio[stock] = portfolio.get(stock, 0) + quantity
        total_investment += cost
        print(f"Added {quantity} shares of {stock} (${cost})\n")


    print("\n--- Portfolio Summary ---")
    for stock, qty in portfolio.items():
        print(f"{stock}: {qty} shares @ ${stock_prices[stock]} = ${qty * stock_prices[stock]}")
    print(f"Total Investment: ${total_investment}")


    save = input("\nSave this summary to a file? (y/n): ").lower()
    if save == "y":
        with open("portfolio_summary.txt", "w") as f:
            f.write("--- Portfolio Summary ---\n")
            for stock, qty in portfolio.items():
                f.write(f"{stock}: {qty} shares @ ${stock_prices[stock]} = ${qty * stock_prices[stock]}\n")
            f.write(f"Total Investment: ${total_investment}\n")
        print("Saved to portfolio_summary.txt")

if __name__ == "__main__":
    track_portfolio()
