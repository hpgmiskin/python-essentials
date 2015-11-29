import utilities

# There are a number of complex data structures


# Lists - ordered collection of variables
# ======================================================================
utilities.printHeading('Lists')

integerList = [1,2,3,4]
stringList = ['one','two','three']

# Add an element to a list
integerList.append(10)
print(integerList)

# Access an element from a list
print(stringList[0])

# Access a sub list
print(stringList[0:2])

# Dictionaries - key value pairs
# ======================================================================
utilities.printHeading('Dictionaries')

myDictionary = {'one':1,'two':2}

# Access an element of a dictionary
print(myDictionary['one'])

# Add an element to a dictionary
myDictionary['three'] = 3
print(myDictionary)

# Sets - unordered collections of variables
# ======================================================================
utilities.printHeading('Sets')
firstSet = {1,2}
secondSet = {2,3}

# Set intersection
print(firstSet & secondSet)

# Set union
print(firstSet | secondSet)

# Set subtraction
print(firstSet - secondSet)