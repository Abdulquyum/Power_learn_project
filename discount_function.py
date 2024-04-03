price = int(input("Enter price of goods: "))
discount_percent = int(input("Enter discount percentage: "))
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = price * (discount_percent / 100)
        discounted_price = price - discount
        return discounted_price
    else:
        return price

calc_discount = calculate_discount(price, discount_percent)
print("Total Amount: {}".format(calc_discount))
