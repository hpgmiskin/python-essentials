
def printHeading(name):

    line = 80
    count = int((line - len(name)) / 2)
    count = count - 1

    print('='*count,' {} '.format(name),'='*count)