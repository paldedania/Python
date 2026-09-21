# Problem 5: Apply a 20% discount when the price is at least 2000.
#
# IPO MODEL
# Input: The item's price.
# Processing: If price >= 2000, subtract a 20% discount; otherwise keep it.
# Output: The final price.
#
# ALGORITHM
# 1. Start.
# 2. Read price.
# 3. If price >= 2000, set final_price to price * 0.80.
# 4. Otherwise, set final_price to price.
# 5. Print final_price.
# 6. Stop.
#
# DRY RUNS
# Case 1: price=2500 -> discount applies -> final_price=2000 -> output 2000.0.
# Case 2: price=1500 -> no discount -> final_price=1500 -> output 1500.0.

price = float(input())

if price >= 2000:
    final_price = price * 0.80
else:
    final_price = price

print(final_price)
