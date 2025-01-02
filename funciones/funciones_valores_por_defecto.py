def calculate_total(price, tax=0.05, discount=0):
    return price + (price * tax) - discount

total = calculate_total(100, 0.08, 10)

print("Total", total)

total = calculate_total(200, 0.08)

print("Total", total)

total = calculate_total(100)

print("Total", total)

total = calculate_total(
    price=500,
    tax=0.02,
    discount=20
)

print("Total", total)