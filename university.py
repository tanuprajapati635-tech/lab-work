percentage = float(input("Enter 12th percentage: "))
math = input("Studied Mathematics? (yes/no): ")
entrance = int(input("Enter entrance score: "))

if percentage < 75:
    print("Not eligible: Less than 75%")
elif math != "yes":
    print("Not eligible: Mathematics required")
elif entrance < 80:
    print("Not eligible: Entrance score less than 80")
else:
    print("Eligible for Admission")