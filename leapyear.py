year=int(input("Input the year to be checked:"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("It is a Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("It is a Leap Year")
else:
    print("Not a Leap Year")
    
