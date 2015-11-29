import math

# Functions package sections of code together
def degree(x):
    "takes an argument x in radian and returns the corresponding value in degrees"

    return (x*360)/(2*math.pi)


print(degree(math.pi))
print(degree(math.pi/2))


# Convert a list of tempuratures
for i in range(9):
    radian = i * (math.pi/4)
    print(radian,' ',degree(radian))