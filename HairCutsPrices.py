hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

for price in prices:
  total_price =+ price
  
average_price = total_price / len(prices)

print("Average Haircut Price: " + str(average_price))

new_prices = []

for price in prices:
  new_prices.append(price - 5)

print("\n" + str(new_prices))
total_revenue = 0

for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]

print("\nTotal Revenue: " + str(total_revenue))

print("\nAverage Daily Revenue: " + str(total_revenue / 7))

cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if prices[i] < 30]

print("\n" + str(cuts_under_30))

