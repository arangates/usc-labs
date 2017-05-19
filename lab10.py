import re

# Open a file
f = open("in.txt")  # open in.txt
temp = f.read()  # store file content in a variable

# write out1

out1 = temp.split()  # replace multiple spaces with single space

with open('out1.txt', 'w') as o1:
    o1.write('String\t\t\tString Number\n\n')
    for index, item in enumerate(out1):
        # print str(index + 1) + "\t\t\t" + str(item)
        o1.write(str(item) + "\t\t\t\t\t" + str(index + 1) + '\n')

# write out2

out2 = ' '.join(temp.split())  # replace multiple spaces with single space
out2 = re.sub(r'\bthe\b', 'THE', out2)  # regex to convert exact 'the' to 'THE'
out2 = out2.split()

with open('out2_the.txt', 'w') as o2:
    o2.write('String\t\t\tString Number\n\n')
    for index, item in enumerate(out2):
        # print str(index + 1) + "\t\t\t" + str(item)
        o2.write(str(item) + "\t\t\t\t\t" + str(index + 1) + '\n')

# write out3

# DIY keerthana :p
