day=int(input("Enter a day (number 1-31):"))
month=int(input("Enter a month (number 1-12):"))
if day==1 and month==1:
    print("New year’s day")
elif day==1 and month==7:
    print("Canada day")
elif day==25 and month==12:
    print("Christmas day")
else:
    print("the entered month and day do not correspond to a fixed-date holiday.")