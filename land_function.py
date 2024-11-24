def sotok(a,b):
    return (a*b)/435.6

lenth=float(input("Enter the lenth for your land:"))
width=float(input("Enter the width for your land:"))

area_in_sotok = sotok(lenth,width)
print(f"The area of your land is:{area_in_sotok:.2f}sotok") 

