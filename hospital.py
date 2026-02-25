
        print("Wrong username or password")
        attempt += 1

if attempt == 3:
    print("Account Locked")age = int(input("Enter age: "))
heart_rate = input("Heart rate abnormal (yes/no): ")
injury = input("Severe injury (yes/no): ")

if heart_rate == "yes" or injury == "yes":
    print("Priority: Critical")

elif age > 65:
    print("Priority: Moderate upgraded to High")

else:
    print("Priority: Normal")