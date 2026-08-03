balance = int(input("Enter your account balance: "))
amount = int(input("Enter withdrawal amount: "))
daily_limit = 25000

if amount > daily_limit:
    print("Withdrawal failed! Daily withdrawal limit exceeded.")
elif amount % 100 != 0:
    print("Withdrawal failed! Amount must be a multiple of 100.")
elif amount > balance:
    print("Withdrawal failed! Insufficient balance.")
else:
    balance = balance - amount
    print("Withdrawal successful!")
    print("Remaining balance:", balance)