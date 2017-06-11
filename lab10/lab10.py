import random
import re

f=open("in2.txt")
temp=f.read()
out1=temp.split()
#Problem1
with open("out1.txt","w") as o1:
	o1.write("String\t\t\t\tStringNumber\n")
	for index,item in enumerate(out1,1):
		o1.write(str(item)+"\t\t\t\t"+str(index)+"\n")
#problem2
out3=' '.join(temp.split())
out2=re.sub(r'\bthe\b', 'THE', out3)
out2=out2.split()
with open("out2.txt","w") as o2:
	o2.write("String\t\t\t\tStringNumber\n")
	for index, item in enumerate(out2,1):
		o2.write(str(item)+"\t\t\t\t"+str(index)+"\n") 
#problem3
out3=out3.split(". ")
with open("out3.txt","w") as o3:
	#o3.write("Randomly Selected string\t\t\t\tLine Number\n")
	for index,item in enumerate(out3,1):
		o3.write(str(index)+"."+"\t"+str(item)+"\n\n")
	o3.write("Randomly Selected String\t\t\t\tLine Number\n")
	#s=set(out3)

#print ("\n".join(random.sample(out2,10)))
	#RandtempList = []
	final = {}
	l = len(out3)
	a= random.sample(range(0,l-1),10)
	print (a)
	for i in a:
		#o3.write(str(out2[i])+"\t\t\t\t"+str(i+1)+"\n")
		s=random.sample(out3,10)
		print (i, " Value of i in each iteration")
		print (len(s)," Length of s")
		sentence = s[i]
		words = sentence.split(" ")
		j = random.randrange(len(words))
		#print (words,'Yaaay')
		#RandtempList.append(words[j])
		#print (RandtempList)
		final[str(i)] = words[j]
		print (final)
	#print (s,'Hellloooo')
	#print (str(s[i]))
	
