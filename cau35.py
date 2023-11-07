n=int(input("Enter human years:"))
a=10.5
if 0<n<=2:
    print("=",a*n,"dog years",)
elif n>2:
    print("=",(a*2+(n-2)*4),"dog years")
else:
    print("Error")