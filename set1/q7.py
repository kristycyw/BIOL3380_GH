#!/usr/bin/python

#script by Kristy Chang

print "Question 7"
def multiply_elements(thelist):
	ans=thelist[0]*thelist[len(thelist)-1]
	print ans

alist=[]
for number in range(5):
        number=int(raw_input("Please input 5 numbers, one at a time: "))
        alist.append(number)
multiply_elements(alist)
