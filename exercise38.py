month=(int(input('Month:')))
year  =(int(input('Year:')))
if month==1 or month==3 or month==5 or month==7 or month ==8 or month==10 or month==12:
     print('31 days')
if month ==4 or month==6 or month==9 or month==11:
        print('30 days')
if month==2:
    if year%4==0:
         print('29 days')
    else:
         print('28 days')
if month<1 or month>12:
    print('Invalid input')        