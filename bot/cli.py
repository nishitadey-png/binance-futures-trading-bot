import argparse
from .client import get_client
from .orders import place_order
from .logging_config import setup_logger

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    logger = setup_logger("bot", "logs/trading.log")
    client = get_client()

    print("\nOrder Request Summary:")
    print(vars(args))

    try:
        order = place_order(
            client,
            logger,
            args.symbol.upper(),
            args.side.upper(),
            args.type.upper(),
            args.quantity,
            args.price
        )

        print("\nOrder Successful ✅")
        print(f"Order ID: {order.get('orderId')}")
        print(f"Status: {order.get('status')}")
        print(f"Executed Qty: {order.get('executedQty')}")
        print(f"Avg Price: {order.get('avgPrice', 'N/A')}")

    except Exception as e:
        print(f"\nOrder Failed ❌: {e}")

if __name__ == "__main__":
    main()
