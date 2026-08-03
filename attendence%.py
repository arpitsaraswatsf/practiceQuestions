n = int(input("Enter number of employees: "))
present_count = 0
for i in range(n):
    attendance =input("is present (1 for present, 0 for absent): ")
    if attendance == "0":
        continue
    present_count += 1
    attendance_percentage = (present_count / n) * 100
    print(f"Attendance percentage of present empployees: {attendance_percentage:.2f}%")