#!/usr/bin/python

#script by Kristy Chang

print "Question 6"
while True:
	inputno=raw_input("Please input positive integers, one at a time, enter 'stop' when done: ")
	if inputno == "stop":
		break
	inputno = int(inputno)
	if inputno%2 == 0:
		print "your number is EVEN"
		half=float(inputno)/2
		print "half of your number is",half 
	elif inputno%2 > 0:
		print "your number is ODD"
		twice=inputno*2
		print "twice of your number is",twice
