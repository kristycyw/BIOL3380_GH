#!/usr/bin/python

#script by Kristy Chang

print "Question 3"
e=raw_input("Enter the name of friend1: ")
f=input("Enter the age of friend1: ")
k=f+5
dict1={"Name": e, "Age": f, "Age in five yrs":k}
#print dict1
g=raw_input("Enter the name of friend2: ")
h=input("Enter the age of friend2: ")
l=h+5
dict2={"Name": g, "Age": h, "Age in five yrs":l}
i=raw_input("Enter the name of friend3: ")
j=input("Enter the age of friend3: ")
m=j+5
dict3={"Name": i, "Age": j, "Age in five yrs":m}

print "friend1 is", dict1["Name"], "she is", dict1["Age"], "years old and will be", dict1["Age in five yrs"], "in five years' time"
print "friend2 is", dict2["Name"], "she is", dict2["Age"], "years old and will be", dict2["Age in five yrs"], "in five years' time"
print "friend3 is", dict3["Name"], "she is", dict3["Age"], "years old and will be", dict3["Age in five yrs"], "in five years' time"
