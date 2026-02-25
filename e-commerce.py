cart = float(input("Enter cart value: "))
member = input("Enter membership (Silver/Gold/Platinum): ")
festival = input("Festival season? (yes/no): ")

discount = 0

# membership discount
if member == "Silver":
    discount = 10
elif member == "Gold":
    discount = 20
elif member == "Platinum":
    discount = 30

# festival discount
if festival == "yes":
    discount = max(discount, 25)

final_amount = cart - (cart * discount / 100)

print("Discount =", discount, "%")
print("Final amount =", final_amount)