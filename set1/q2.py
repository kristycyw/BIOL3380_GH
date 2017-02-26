#!/usr/bin/python

#script by Kristy Chang

print "Question 2"
a=input("1st number: ")
b=input("2nd number: ")
c=input("3rd number: ")
d=input("4th number: ")
mylist=[a,b,c,d]

sumoflist=sum(mylist)
#print sumoflist

newlist=[mylist[0]*mylist[1],mylist[2]*mylist[3]]
#print newlist

print "The list of numbers you gave was", mylist, "the sum of the list was", sumoflist, "and the new list that is the product of each pair of elements in the original list is", newlist 

