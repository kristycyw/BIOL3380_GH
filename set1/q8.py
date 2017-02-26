#!/usr/bin/python

#script by Kristy Chang

myfile=open('/home/kristy/Desktop/BIOL3380/numbers.txt',"r")
outputmaxmin=open('/home/kristy/Desktop/BIOL3380/outputmaxmin.txt',"w")

def maxmin(lists):
	#here is where i could use the functions min() and max()
	low =int(lists[0])
	for i in lists:
		temp_i = int(i)
		if temp_i < low:
			low = temp_i
	high =int(lists[0])
	for i in lists:
		temp_i= int(i)
		if temp_i > high:
			high = temp_i
	return low, high

#x=[1,2,3,4,4,6,7,8]
#print maxmin(x)

for line in myfile:
	myline=line.strip().split("\t")
#	print myline
	mymaxmin=maxmin(myline)
#	print mymaxmin
	outputmaxmin.write("The minimum and maximum elements on this line are %i, %i respectively\n"%mymaxmin)

myfile.close
outputmaxmin.close
print "done"
