from market_data import get_market_data


def check_market():

    data = get_market_data()

    if not data:
        print("❌ No market data")
        return

    print("✅ Market data available")
    print(f"Symbols found: {len(data)}")

    for item in data[:3]:
        print(item)


if __name__ == "__main__":
    check_market()
