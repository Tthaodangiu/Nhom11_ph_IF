a=int(input('Number of sides:'))
if a==3:
    print('The shape with', a ,'sides is a triangle.')
elif a==4:
    print('The shape with', a ,'sides is a quadrilateral.')
elif a==5:
    print('The shape with', a ,'sides is a pentagon.')
elif a==6:
    print('The shape with', a ,'sides is a hexagon.')
elif a==7:
    print('The shape with', a ,'sides is a heptagon.')
elif a==8:
    print('The shape with', a ,'sides is an octagon.')
elif a==9:
    print('The shape with', a ,'sides is a nonagon.')
elif a==10:
    print('The shape with', a ,'sides is a decagon.')
else:
    print('Invalid number of sides. Valid shapes have 3 to 10 sides.')