"""A simple portfolio calculator using manually defined example prices."""

import csv
from pathlib import Path

# Sample prices for demonstration only; these are not live market prices.
STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "MSFT": 420.00,
    "GOOGL": 165.00,
    "AMZN": 190.00,
}


def read_quantity() -> int:
    while True:
        raw_quantity = input("Quantity: ").strip()
        try:
            quantity = int(raw_quantity)
        except ValueError:
            print("Enter a whole-number quantity.")
            continue
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue
        return quantity


def collect_holdings() -> list[dict[str, float | int | str]]:
    holdings: list[dict[str, float | int | str]] = []
    print("\nAvailable symbols:", ", ".join(sorted(STOCK_PRICES)))
    print("Enter 'done' when you have finished adding holdings.")

    while True:
        symbol = input("Stock symbol: ").strip().upper()
        if symbol == "DONE":
            break
        if symbol not in STOCK_PRICES:
            print("That symbol is not in the sample price list.")
            continue

        quantity = read_quantity()
        price = STOCK_PRICES[symbol]
        value = price * quantity
        holdings.append({
            "symbol": symbol,
            "unit_price": price,
            "quantity": quantity,
            "holding_value": value,
        })
        print(f"Added {quantity} share(s) of {symbol}: ${value:,.2f}")

    return holdings


def display_summary(holdings: list[dict[str, float | int | str]]) -> float:
    print("\nPORTFOLIO SUMMARY")
    print("-" * 62)
    print(f"{'Symbol':<12}{'Price':>14}{'Quantity':>14}{'Value':>18}")
    print("-" * 62)

    total = 0.0
    for holding in holdings:
        price = float(holding["unit_price"])
        quantity = int(holding["quantity"])
        value = float(holding["holding_value"])
        total += value
        print(f"{holding['symbol']:<12}${price:>13,.2f}{quantity:>14}${value:>17,.2f}")

    print("-" * 62)
    print(f"{'Total investment value:':<40}${total:>21,.2f}")
    print("Note: prices are hardcoded examples, not live market data.")
    return total


def save_csv(holdings: list[dict[str, float | int | str]], total: float) -> Path:
    output_path = Path("portfolio_summary.csv")
    fieldnames = ["symbol", "unit_price", "quantity", "holding_value"]
    with output_path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(holdings)
        writer.writerow({"symbol": "TOTAL", "holding_value": total})
    return output_path


def main() -> None:
    print("Stock Portfolio Tracker")
    holdings = collect_holdings()
    total = display_summary(holdings)

    if holdings and input("Save this summary to CSV? (y/n): ").strip().lower() == "y":
        saved_path = save_csv(holdings, total)
        print(f"Summary saved to {saved_path.resolve()}")


if __name__ == "__main__":
    main()
