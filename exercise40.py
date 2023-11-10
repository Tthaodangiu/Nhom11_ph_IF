Side_1=float(input(""))
Side_2=float(input(""))
Side_3=float(input(""))
if Side_1==Side_2==Side_3:
    print("an equilateral triangle")
elif Side_1==Side_2!=Side_3 or Side_1==Side_3!=Side_2 or Side_2==Side_3!=Side_1:
    print("an isosceles triangle")
else:
    print("a scalene triangle")

    
    