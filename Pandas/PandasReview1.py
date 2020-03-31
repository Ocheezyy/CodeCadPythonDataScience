import codecademylib
import pandas as pd

orders = pd.read_csv("shoefly.csv")

print(orders.head(5))

emails = orders["email"]

print(emails)

frances_palmer = orders[(orders.first_name == "Frances") & (orders.last_name == "Palmer")]

print(frances_palmer)

comfy_shoes = orders[orders.shoe_type.isin(['clogs', 'boots', 'ballet flats'])]