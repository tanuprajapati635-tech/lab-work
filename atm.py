balance = int(input("Enter account balance: "))
withdraw = int(input("Enter withdrawal amount: "))
atm_cash = int(input("Enter ATM cash available: "))

if withdraw > balance:
    print("Insufficient Balance")

elif withdraw > 50000:
    print("Daily limit exceeded")

elif withdraw > atm_cash:
    print("ATM has insufficient cash")

else:
    print("Withdrawal successful")
    balance = balance - withdraw
    print("Remaining balance =", balance)