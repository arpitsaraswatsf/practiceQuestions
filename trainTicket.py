# Train Ticket Booking System

age = int(input("Enter passenger age: "))
travel_class = input("Enter class (Sleeper/AC): ")

# Base fare
if travel_class.lower() == "sleeper":
    fare = 500
elif travel_class.lower() == "ac":
    fare = 1000
else:
    print("Invalid class selected.")
    exit()

# Senior citizen discount (60 years and above)
if age >= 60:
    discount = fare * 0.20   # 20% discount
    fare = fare - discount
    print("Senior Citizen Discount Applied: ₹", discount)

print("Total Ticket Fare = ₹", fare)