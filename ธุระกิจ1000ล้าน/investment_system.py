import yfinance as yf
import base64

print("==== PREMIUM STOCK SYSTEM ====")

key = input("Enter Access Key: ")

valid_keys = [
    "INV-7845-ABCD",
    "INV-9921-XKLP",
    "INV-1134-QWER",
    "INV-5567-ZXCV"
]

if key in valid_keys:

    print("✅ Access Granted\n")

    print("📊 Today's Stock Recommendation")
    print("--------------------------------")

    stocks = ["AAPL","TSLA","NVDA","MSFT","AMZN","META"]

    for s in stocks:

        data = yf.Ticker(s).history(period="2d")

        if len(data) >= 2:

            yesterday = data["Close"].iloc[-2]
            today = data["Close"].iloc[-1]

            change = today - yesterday

            if change > 0:
                signal = "BUY 📈"
            else:
                signal = "WAIT ⏳"

            print(f"{s} | Price: {round(today,2)} | Change: {round(change,2)} | {signal}")

else:
    print("❌ Access Denied")