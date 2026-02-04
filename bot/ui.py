import streamlit as st
from bot.client import get_client
from bot.orders import place_order
from bot.logging_config import setup_logger

st.set_page_config(page_title="Trading Bot", layout="centered")

st.title("Binance Futures Trading Bot (Testnet / Mock)")

symbol = st.text_input("Symbol", value="BTCUSDT")
side = st.selectbox("Side", ["BUY", "SELL"])
order_type = st.selectbox("Order Type", ["MARKET", "LIMIT"])
quantity = st.number_input("Quantity", min_value=0.0001, value=0.01)

price = None
if order_type == "LIMIT":
    price = st.number_input("Limit Price", min_value=1.0, value=45000.0)

if st.button("Place Order"):
    logger = setup_logger("ui", "logs/trading.log")
    client = get_client()

    try:
        order = place_order(
            client,
            logger,
            symbol.upper(),
            side,
            order_type,
            quantity,
            price
        )

        st.success("Order placed successfully!")
        st.json({
            "orderId": order.get("orderId"),
            "status": order.get("status"),
            "executedQty": order.get("executedQty"),
            "avgPrice": order.get("avgPrice", "N/A")
        })

    except Exception as e:
        st.error(f"Order failed: {e}")
