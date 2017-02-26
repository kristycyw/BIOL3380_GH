#!/usr/bin/python

#script by Kristy Chang

print "Question 5a"
number_list=[]
for number in range(4):
	number=int(raw_input("Please input 4 numbers, one at a time: "))
	number_list.append(number)
sumoflist=sum(number_list)
print "The sum of your numbers is", sumoflist
new_num_list=[]
for i in range(0,len(number_list),2):
	newnum=number_list[i]*(number_list[i+1])
	new_num_list.append(newnum)
print new_num_list

print "Question 5b"
number_list2=[]
while True:
	number2=raw_input("Please input positive integers, one at a time, enter 'stop' when done: ")
	if number2 == "stop":
		break
	number2 = int(number2)
	if number2 >0:
		 number_list2.append(number2)
sumoflist2=sum(number_list2)
print "The sum of your numbers is",sumoflist2

new_num_list2=[]
for i in range(0,len(number_list2),2):
        newnum2=number_list2[i]*(number_list2[i+1])
        new_num_list2.append(newnum2)
print new_num_list2

