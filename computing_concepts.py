import utilities
# Basic computing concepts

# Iteration
# ======================================================================
utilities.printHeading('Itteration')

# For loop
for i in range(10):
    print(i)


# While loop
index = 0
while (index < 10):
    print(index)
    index = index + 2

# Selection
# ======================================================================
utilities.printHeading('Selection')

# If statement
if True:
    print('True is True')
else:
    print('True is not True')

# Boolean logic
print('10 > 9 is',(10 > 9))
print('2 == 2 is',(2 == 2))
print('2 == 3 is',(2 == 3))

# Boolean logic in if statement
ten = 10
if (ten > 9):
    print('{} > 9'.format(ten))




