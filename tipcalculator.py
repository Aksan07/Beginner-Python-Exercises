print("Welcome to the tip calculator")
bill=float(input("What is the total bill?\n$"))
tip_percentage=int(input("What percentage tip would you like to give 10,12 or 15?\n"))
tipped_bill=bill+(bill*(tip_percentage/100))
people=int(input("How many people to split the bill?"))
each_person_share=round(tipped_bill/people,2)
print(f"Each person should pay ${each_person_share}")

