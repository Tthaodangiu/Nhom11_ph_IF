day=int(input("Enter a day (number):"))
month=int(input("Enter a month (number):"))
if day==1 and month==1:
    print("New year’s day")
elif day==1 and month==7:
    print("Canada day")
elif day==25 and month==12:
    print("Christmas day")
else:
    print("the entered month and day do not correspond to a fixed-date holiday.")