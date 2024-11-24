def lengths(a):
    x= (a*12)/12
    return x

def heights(a):
    i= (a*12)/5
    return i

length= int(input("Ënter your wall's length in feet: "))
height= int (input("Enter your wall's height in feet: "))

print(f"In length you need: {lengths(length)} bricks")
print(f"In height you need: {heights(height)} bricks")
print(f"You need total: {(lengths(length))*(heights(height))} bricks to complete the wall")