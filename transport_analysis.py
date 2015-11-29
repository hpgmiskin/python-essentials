with open('london_transport.csv') as openFile:
    lines = openFile.readlines()


headers = {heading:index for index,heading in enumerate(lines.pop(0).split(','))}


print(headers)

for line in lines:

    print(line[headers['PedalCycles']])

