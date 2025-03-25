def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    else:
        return price

original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

final_price = calculate_discount(original_price, discount_percent)

if discount_percent >= 20:
    print(f"The final price after applying a {discount_percent:.2f}% discount is ${final_price:.2f}")
else:
    print(f"No discount applied. The original price is ${original_price:.2f}")