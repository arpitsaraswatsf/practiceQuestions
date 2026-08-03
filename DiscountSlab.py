total_amount = float(input("Enter total amount: "))


if total_amount < 1000:
    discount = total_amount + 0
    print("discount is 0%: ", discount)
elif 1000 <= total_amount < 5000:
    discount = total_amount * 0.2
    print("discount is 20%: ", discount)
elif 5000 <= total_amount < 7000:
    discount =  total_amount * 0.3
    print("discount is 30%: ", discount)

print(f"Final amount to be paid: {total_amount - discount}")
