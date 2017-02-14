#!/usr/bin/python

#script by Kristy Chang

print "Question 4"
n=float(5)/7
#The division of an integer by an integer in python results in an integer. Since 5/7 is smaller than 1, rounding to the closest integer will result in 0. This is not a problem in python3.

randomlist=[1,2,3,4,5]
print randomlist, "5th element is", randomlist[4]
#The list calls from 0 onward, randomlist[0] calls the first element of the list and so on, calling randomlist[5] will result in an IndexError since it calls a nonexistent 6th element of the list

randomdict= {"key1":randomlist, "key2":2}
#print randomdict["key3"] 
#Causes a KeyError message to appear, this occurs when a dict() object is requested and the key is not in the dictionary

print randomdict["key1"]
#prints the list with no problems, calling the key calls all the info related to it.
