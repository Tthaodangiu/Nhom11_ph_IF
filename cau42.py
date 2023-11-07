n=float(input("Enter frequency here: "))
if 0<=(n-261.63)<=1:
    print('C4')
elif 0<=(n-293.66)<=1:
    print('D4')
elif 0<=(n-329.63)<=1:
    print('E4')
elif 0<=(n-349.23)<=1:
    print('F4')
elif 0<=(n-392)<=1:
    print('G4')
elif 0<=(n-440)<=1:
    print('A4')
elif 0<=(n-493.88)<=1:
    print('B4')
else:
    print('Invalid')