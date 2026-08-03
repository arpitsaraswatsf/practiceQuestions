# CHECK LOAN ELIGIBILTY BASED ON *INCOME, CREDIT SCORE, AND EMI EXISTENCE


# age = int(input("Enter age: "))
# income = float(input("ENter income/month: "))
# cr_score = int(input("Enter credit schore: "))
# run_emi = input("Do you have any existing EMIs? (yes/no): ")

# eligible  = True

# if age <21:
#     eligible = False
#     print("age is below 21")

# if income < 25000:
#     eligible = False
#     print("income is below 25k")

# if cr_score < 680:
#     eligible = False
#     print("credit score is below 680")

# if run_emi == "no":
#     eligible = False
#     print("you have existing EMIs")

# if eligible:
#     print("you are eligible for loan")

# else:
#     print("loan rejected")



# Q-2: To calculate the final bill for an e-commerce order by applying discount slabs using
# an elif ladder

# total_amount = float(input("Enter total amount: "))


# if total_amount < 1000:
#     discount = total_amount + 0
#     print("discount is 0%: ", discount)
# elif 1000 <= total_amount < 5000:
#     discount = total_amount * 0.2
#     print("discount is 20%: ", discount)
# elif 5000 <= total_amount < 7000:
#     discount =  total_amount * 0.3
#     print("discount is 30%: ", discount)

# print(f"Final amount to be paid: {total_amount - discount}")


# Q-3: To calculate attendance percentage of present employees, using a loop with
# 'continue' to skip absent-marked records.

n = int(input("Enter number of employees: "))
present_count = 0
for i in range(n):
    attendance =input("is present (1 for present, 0 for absent): ")
    if attendance == "0":
        continue
    present_count += 1
    attendance_percentage = (present_count / n) * 100
    print(f"Attendance percentage of present empployees: {attendance_percentage:.2f}%")