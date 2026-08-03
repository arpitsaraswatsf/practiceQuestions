age = int(input("Enter age: "))
income = float(input("Enter income/month: "))
cr_score = int(input("Enter credit score: "))
run_emi = input("Do you have any existing EMIs? (yes/no): ")

eligible  = True

if age <21:
    eligible = False
    print("age is below 21")

if income < 25000:
    eligible = False
    print("income is below 25k")

if cr_score < 680:
    eligible = False
    print("credit score is below 680")

if run_emi == "yes":
    eligible = False
    print("you have existing EMIs")

if eligible:
    print("you are eligible for loan")

else:
    print("loan rejected")
