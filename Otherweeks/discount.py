from datetime import datetime, timedelta

subtotal = float(input("Enter the subtotal of your purchase:"))
current_date = datetime.now()
date_num = datetime.weekday(current_date)
# setting for Monday
#date_num = 0
discount_rate = 0.1
saletax_rate = 0.06

if (date_num == 1 or date_num == 2) and (subtotal >= 50):
    discount_amt = subtotal * discount_rate
    print(f"Discount amount: {discount_amt:.2f}")
    #subtotal = subtotal - discount_amt
    subtotal -= discount_amt
else:
    additional_spend = 50 - subtotal
    print(f"The amount to spend to get discount is: {additional_spend:.2f}")

tax_amt = subtotal * saletax_rate
print(f"Sales tax amount: {tax_amt:.2f}")
total = subtotal + tax_amt
print(f"Total: {total:.2f}")
