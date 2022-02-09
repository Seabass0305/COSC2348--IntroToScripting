"""
Question 1
----------
Code Description: This snippet of code prints two specific patterns of stars

Author: Manuel Sebastian Hernandez
Date: February 4th, 2022
""" 

# Question 1a

def Question_1():
	star = "*"
	for i in range(1, 6):
		for l in range(0, i):
			print(star, end = ' ')
		print("\n")

# Question 1b

	emptyStar = " "	
	count = 4
	for indxOne in range(1, 6):
		for indxTwo in range(0, count):
			print(emptyStar, end = ' ')
		count -= 1
		for indxThree in range(0, indxOne):
			print(star, end = ' ')	
		print("\n")

Question_1()

print("\n")

"""
Question 2
----------
Code Description: This snippet of code takes in user input
				  and uses the two integers in a mathematic
				  formula that includes factorials
""" 

def Question_2(n, r):

	num1 = factorial(n) / (factorial(r) * (factorial(n-r)))

	print("\nThe result for the problem: n! / r! * (n - r)!  is", num1, "\n")

	num2 = factorial(n) / (factorial(n-r))

	print("The result for the problem: n! / (n - r)! is", num2, "\n")


# The following code is a basic recursive method that 
# calculates and returns the factorial of a number
# that is passed.

def factorial(x):
	if x > 1:
		return x * factorial(x-1)
	else:
		return 1;

# Printing to Screen

n = int(input("Please enter a number: "))
r = int(input("Please enter another number: "))

Question_2(n, r)

print("\n")

"""
Question 3
----------
Code Description: This snippet of code takes and sorts a list in order of
				  ascending numeric value
""" 

def Question_3(startingList):
	newList = []

	print("Starting List: ", startingList, "\n")
	
	for j in range(1, len(startingList)+1):
		smallest = startingList[0]
		for i in range(0, len(startingList)-1):
			if smallest > startingList[i+1]:
				smallest = startingList[i+1]
		newList.append(smallest)
		startingList.remove(smallest)

	print("Sorted List: ", newList, "\n")

list_Q3 = [20, 68, 41, 88, 16, 40, 65, 97, 85]

Question_3(list_Q3)

print("\n")

"""
Question 4
----------
Code Description: This snippet of code takes a list and then determines
				  the sum of all elements in the list, creates a new list
				  with all of the even numbers in the list, and finally,
				  creates another list containing all the odd numbers.
""" 

def sumOf(passedList):
	sumOfList = 0
	for i in range(0, len(passedList)):
		sumOfList += passedList[i]
	return sumOfList

def Question_4():
	mainList = [20, 68, 41, 88, 16, 40, 65, 97, 85]
	oddList, evenList = [], []

	for i in range(0, len(mainList)):
		if mainList[i] % 2 == 0:
			evenList.append(mainList[i])
		elif mainList[i] % 2 == 1 or mainList[i] == 1:
			oddList.append(mainList[i])

	print("This is the list for problem 4:", mainList, "\n")

	print("This is the sum of all elements in the list:", sumOf(mainList), "\n")

	print("These are the even numbers in the list:", evenList, "\n")

	print("This is the sum of all even numbers in the list:", sumOf(evenList), "\n")

	print("These are the odd numbers in the list:", oddList, "\n")

	print("This is the sum of all odd numbers in the list:", sumOf(oddList), "\n")

Question_4()

print("\n")

"""
Question 5
----------
Code Description: This snippet of code finds all prime numbers between 2 and 50
				  using loops.
""" 

def Question_5(): 
	primeList = []
	minimum = 2
	maximum = 50
	
	while minimum <= maximum:
		flag = True
		for i in range(2, minimum):
			if minimum % i == 0:
				flag = False
		if flag:
			primeList.append(minimum)
		minimum += 1

	print(primeList)


Question_5()

print("\n")

"""
Question 6
----------
Code Description: This snippet of code calls a reworked version
				  of problems 1, 2, and 3 passing variables or
				  calling their methods this time around.
""" 

def Question_6():
	Question_1()

	print("\n")

	n = int(input("Please enter a number: "))
	r = int(input("Please enter another number: "))
	Question_2(n, r)

	print("\n")

	passList = [90, 68, 41, 88, 16, 40]
	Question_3(passList)

Question_6()

print("\n")

"""
Question 7
----------
Code Description: 


""" 

#def Question_7():



#Question_7()

"""
Question 8
----------
Code Description: 


""" 

#def Question_8():



#Question_8()

"""
Question 9
----------
Code Description: This question gives us a snippet of code and asks us to fix the
				  output to print even numbers by editing the code.
""" 

def Question_9():
	loop_counter = 1
	while loop_counter <= 10:
		#print(loop_counter)        #removing the first print statement fixes the code
		if loop_counter%2 == 0:
			print(loop_counter, end = ' ')
		loop_counter += 1 			#Here we are increasing loop count by 1
	print("\n")

Question_9()

