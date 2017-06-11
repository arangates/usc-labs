import collections

#empty dictionary
dict = {}
dict2 = {}

#read input file
f = open("input.txt")
alpha_list = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

val = 0
for line in f:
    new = []
    #print (val)
    inputline = line.split(" ")
    #print (len(inputline))
    #print (inputline)
    for i in range(len(inputline)):
        if inputline[i] == '1':
            new.append(alpha_list[i])
    #print (new)
    dict[val] = new
    dict2[alpha_list[val]] = new
    #print (dict2)
    val += 1

#print ("Matrix in characters:\n", dict)
dict2 = collections.OrderedDict(sorted(dict2.items()))
#print dict2)

inp1 = input('Input1: ')
inp2 = input('Input2: ')
#print (inp1,inp2)
lst1 = []
lst2 = []
for i in range(len(alpha_list)):
    #print (i)
    if alpha_list[i] == inp1:
        lst1 += dict[i]
        #print("appended1")
    if alpha_list[i] == inp2:
        lst2 += dict[i]
        #print("appended2")

    #print("List1: ", lst1)
    #print("List2: ", lst2)

    # print ("Task 1 output: ", list(set(lst2).intersection(lst1)))

with open('output.txt', 'w') as o1:
    o1.write("Task 1 output: " + str(list(set(lst2).intersection(lst1))))


# find all path
def find_all_path(graph, start, end, path=[]):
    path = path + [start]
    #print(path)
    if (start == end):
        return [path]
    if not start in graph:
        return None
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_path(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


#print (find_all_path(dict2,inp1,inp2))
lst = find_all_path(dict2, inp1, inp2)

for i in lst:
    l = len(lst) - 1
    if len(i) < l:
        l = i

# print("Task 2 output: ", lst[l])

with open('output.txt', 'a') as o1:
    o1.write("\nTask 2 output: " + str("-".join(str(x) for x in lst[l])))