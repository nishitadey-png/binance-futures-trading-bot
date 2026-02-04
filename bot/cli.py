import typer
from rich import print
from rich.prompt import Prompt, FloatPrompt
from typing import Optional

from .client import get_client
from .orders import place_order
from .logging_config import setup_logger

app = typer.Typer(help="Binance Futures Trading Bot")

def interactive_mode():
    print("[bold cyan]Welcome to Binance Futures Trading Bot[/bold cyan]")

    symbol = Prompt.ask("Enter symbol", default="BTCUSDT").upper()
    side = Prompt.ask("Side", choices=["BUY", "SELL"], default="BUY")
    order_type = Prompt.ask("Order Type", choices=["MARKET", "LIMIT"], default="MARKET")
    quantity = FloatPrompt.ask("Quantity", default=0.01)

    price = None
    if order_type == "LIMIT":
        price = FloatPrompt.ask("Limit Price")

    logger = setup_logger("bot", "logs/trading.log")
    client = get_client()

    print("\n[bold yellow]Order Summary[/bold yellow]")
    print({
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity,
        "price": price
    })

    try:
        order = place_order(
            client,
            logger,
            symbol,
            side,
            order_type,
            quantity,
            price
        )

        print("\n[bold green]Order Successful[/bold green]")
        print(f"Order ID: {order.get('orderId')}")
        print(f"Status: {order.get('status')}")
        print(f"Executed Qty: {order.get('executedQty')}")
        print(f"Avg Price: {order.get('avgPrice', 'N/A')}")

    except Exception as e:
        print(f"\n[bold red]Order Failed[/bold red]: {e}")

@app.command()
def run(
    symbol: Optional[str] = None,
    side: Optional[str] = None,
    order_type: Optional[str] = None,
    quantity: Optional[float] = None,
    price: Optional[float] = None
):
    """
    Run trading bot.
    If no arguments are provided, interactive mode starts.
    """
    if not symbol:
        interactive_mode()
        return

    logger = setup_logger("bot", "logs/trading.log")
    client = get_client()

    try:
        order = place_order(
            client,
            logger,
            symbol.upper(),
            side.upper(),
            order_type.upper(),
            quantity,
            price
        )

        print("\n[green]Order Successful ✅[/green]")
        print(order)

    except Exception as e:
        print(f"[red]Order Failed ❌[/red]: {e}")

if __name__ == "__main__":
    app()
