print("Welcome to the tip calculator")

total_bill = float(input("What is the total bill sir? $"))
tip = int(input("What is the tip amount you want to give? like 10, 12, 15 and 20? "))
number_of_people = int(input("Total how many number of people to split the bill? "))

tip_percentage = tip/100
total_tip_bill = tip_percentage * total_bill
final_amount = total_bill + total_tip_bill
split = final_amount/number_of_people

round_bill_each = round(split)


print(f"Each person payable amount is  ${round_bill_each}")