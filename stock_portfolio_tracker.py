# ============================================
# 📈 STOCK PORTFOLIO TRACKER
# CodeAlpha Python Internship - Task 2
# ============================================

# Predefined stock prices
stock_prices = {
    "AAPL": 180,   # Apple
    "TSLA": 250,   # Tesla
    "GOOGL": 140,  # Google
    "MSFT": 330,   # Microsoft
    "AMZN": 150    # Amazon
}

# Welcome Banner
print("=" * 50)
print("📈      STOCK PORTFOLIO TRACKER")
print("=" * 50)
print("💹 Track your stock investments easily!\n")

# Display available stocks
print("📌 Available Stocks:")
print("-" * 50)
for stock, price in stock_prices.items():
    print(f"🔹 {stock:<6} : ${price}")
print("-" * 50)

# Initialize total investment
total_investment = 0
portfolio_details = []

# Ask user how many stocks they want to enter
n = int(input("\n📝 How many different stocks do you own? "))

# Input stock details
for i in range(1, n + 1):
    print(f"\n📊 Stock Entry #{i}")
    print("-" * 30)

    stock_name = input("🔤 Enter stock symbol (AAPL/TSLA/etc): ").upper()

    if stock_name in stock_prices:
        quantity = int(input("🔢 Enter quantity: "))
        price = stock_prices[stock_name]
        investment = price * quantity
        total_investment += investment

        portfolio_details.append(
            f"{stock_name} - {quantity} shares × ${price} = ${investment}"
        )

        print(f"✅ Added {stock_name} | Investment Value: ${investment}")
    else:
        print("❌ Stock symbol not found! Please try again.")

# Display final summary
print("\n" + "=" * 50)
print("📋 PORTFOLIO SUMMARY")
print("=" * 50)

for detail in portfolio_details:
    print(f"📌 {detail}")

print("-" * 50)
print(f"💰 Total Investment Value: ${total_investment}")
print("=" * 50)

# Save results to a text file
with open("portfolio.txt", "w", encoding="utf-8") as file:
    file.write("STOCK PORTFOLIO SUMMARY\n")
    file.write("=" * 50 + "\n")
    for detail in portfolio_details:
        file.write(detail + "\n")
    file.write("-" * 50 + "\n")
    file.write(f"Total Investment Value: ${total_investment}\n")

print("\n💾 Portfolio details saved successfully to 'portfolio.txt'")
print("🎉 Thank you for using Stock Portfolio Tracker!")