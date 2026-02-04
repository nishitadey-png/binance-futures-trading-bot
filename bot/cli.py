from bot.client import get_client
from bot.orders import place_order
from bot.logging_config import setup_logger
import typer

app = typer.Typer()

@app.command()
def trade():
    symbol = typer.prompt("Symbol (BTCUSDT)").upper()
    side = typer.prompt("Side (BUY/SELL)").upper()
    order_type = typer.prompt("Order Type (MARKET/LIMIT)").upper()
    quantity = float(typer.prompt("Quantity"))

    price = None
    if order_type == "LIMIT":
        price = float(typer.prompt("Price"))

    
    if order_type == "MARKET":
        logger = setup_logger("market", "logs/market_order.log")
    elif order_type == "LIMIT":
        logger = setup_logger("limit", "logs/limit_order.log")
    else:
        typer.echo("Invalid order type")
        raise typer.Exit(1)

    client = get_client()

    order = place_order(
        client=client,
        logger=logger,
        symbol=symbol,
        side=side,
        order_type=order_type,
        quantity=quantity,
        price=price
    )

    typer.echo("\nOrder Successful")
    typer.echo(f"Order ID: {order['orderId']}")
    typer.echo(f"Status: {order['status']}")
    typer.echo(f"Executed Qty: {order['executedQty']}")
    typer.echo(f"Avg Price: {order['avgPrice']}")

if __name__ == "__main__":
    app()
