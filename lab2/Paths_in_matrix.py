#count the number of paths in a matrix from start to end
import collections
#empty dictionary
dict = {}
#read input file
f = open("input.txt")
alpha_list=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
val = 0
for line in f:
        new=[]
        #print (val)
        inputline = line.split(" ")
        #print (len(inputline))
        #print (inputline)
        for i in range(len(inputline)):
                if inputline[i]=='1':
                        new.append(alpha_list[i])
        #print (new)
        #dict[val]=new //print the key values of dict in numbers
        dict[alpha_list[val]]=new #print key values in alphabets
        val+=1

#print ("Matrix in characters:\n", dict)
dict2 = collections.OrderedDict(sorted(dict.items()))
#print (dict2)
end_val=len(dict2)-1
#print (end_val)

#print (alpha_list[end_val])

# find all path
def find_all_path(matrix, start, end, path=[]):
    path = path + [start]
    #print(path)
    if (start == end):
        return [path]
    if not start in matrix:
        return None
    paths = []
    for node in matrix[start]:
        if node not in path:
            newpaths = find_all_path(matrix, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

#print (find_all_path(dict2,inp1,inp2))
count = len(find_all_path(dict2,'A',alpha_list[end_val]))
print ("The Number of Paths found: ",count)

with open('output.txt', 'w') as o1:
    o1.write('The number of paths found: \t'+ str(count))

