# tip calculator

# Welcome message
print("Welcome to the tip calculator!")

# bill amount input
bill = float(input("What was the total bill? $"))

# tip percentage input
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

# split input
people = int(input("How many people to split the bill? "))

# tip / 100
tip_as_percent = tip / 100

# total tip amount
total_tip_amount = tip_as_percent * bill

# total bill with tip
total_bill = bill + total_tip_amount

# bill per person
bill_per_person = total_bill / people

# rounded to 2 decimal places
final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${final_amount}")
