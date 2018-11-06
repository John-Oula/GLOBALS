import math
def area (radius):
    print(22/7*radius*radius)
    return
area(7)

def areas(radius):
    jibu = math.pi*math.pow(radius,2)
    print("area=",jibu)
    return
print("Enter the radius of your circle")
r = float(input())
answer = areas(r)
