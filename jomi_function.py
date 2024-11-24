
def cal_sotok(a,b):
    sotok=(a*b)/435.6
    return sotok

def avg_len(a,b):
    length=(a+b)/2
    return length

ask= int(input("Enter your land's one side length:\n"))
ask2= int(input("Enter your land's other side length:\n"))

avar= avg_len(ask,ask2)

print(f"Your land's avarage length is:{avar:.2f}")

ask3=int(input("Enter your land's one side weight:\n"))
ask4=int(input("Enter your land's another side weight:\n"))

avar2= avg_len(ask3,ask4)
print(f"Your land's avarage weight is:{avar2:.2f}")

print(f"\nYour total land area is: {cal_sotok(avar,avar2):.2f} sotok")

