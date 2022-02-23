import random

"""
Question 1
----------
Code Description: This code is for an Employee Management System
				  that allows for the addition of and editing
				  of employees within a dictionary database.

Author: Manuel Sebastian Hernandez
Date: February 20th, 2022
""" 

def program():

	class Employee:
		"""My Employee Class"""
		def __init__(self, name, department, jobTitle):
			self.name = name
			#self.IDnumber = IDnumber
			self.department = department
			self.jobTitle = jobTitle

		def display(self):
			print(self.name, '\t', self.department, '\t\t', self.jobTitle)
			print('\n')

		def getName(self):
			return self.name

		def setName(self, name):
			self.name = name

		def getDepartment(self):
			return self.department

		def setDepartment(self, department):
			self.department = department

		def getJobTitle(self):
			return self.jobTitle

		def setJobTitle(self, jobTitle):
			self.jobTitle = jobTitle

	emp_1 = Employee('Susan Meyers', 'Accounting', 'Vice President')
	emp_2 = Employee('Mark Jones', 'Manufacturing', 'Engineer')
	emp_3 = Employee('Joy Rogers', 'IT', '\t Programmer')

	employeeDict = {47899 : emp_1, 39119 : emp_2, 81774 : emp_3}


	# Testing Syntax
	# --------------
	# employeeDict['47899'].display()
	# print(checkDict('47840', employeeDict))


	print('\nWelcome to the Employee Management System!')
	print('------------------------------------------')

	flag = True

	while(flag):

		print('1. Look-up an Employee ')
		print('2. Add a new Employee ')
		print("3. Change an Existing Employee's info ")
		print('4. Delete an Employee from the System ')
		print('5. Quit Program\n')

		print("Employee ID's in the System: ", end = '')

		for key, value in employeeDict.items():
			print(key, end = ' ')

		print('\n')

		choice = -1
		empID = 0

		while choice < 1 or choice > 5:
			choice = int(input('\nWhat would you like to do: '))

		# Option 5: Quit the Program

		if choice == 5:
			print('\nGood Bye!')
			flag = False

		# Option 1: Look-up an Employee (Done)

		elif choice == 1:

			empID = int(input('\nPlease enter the Employee ID to search: '))
			
			if empID in employeeDict:
				print('\nID', '\tName', '\t\tDepartment', '\tTitle')
				print('---------------------------------------------------------------')
				print(empID, end = '\t')
				employeeDict[empID].display()
			else:
				print('\nThere is no Employee with that Employee ID!\n')

		# Option 2: Add an Employee (Done)

		elif choice == 2:

			empID = int(input('\nPlease enter the Employee ID to Add to the System: '))

			while empID in employeeDict:
				 empID = int(input('\nPlease enter an Employee ID that is not in the System: '))

			
			tempName = input("\nPlease enter the Employee's Name: ")
			tempDepartment = input("\nPlease enter the Employee's Department: ")
			tempTitle = input("\nPlease enter the Employee's Job Title: ")
			tempEmployee = Employee(tempName, tempDepartment, tempTitle)
			employeeDict[empID] = tempEmployee

			print('\nID', '\tName', '\t\tDepartment', '\tTitle')
			print('---------------------------------------------------------------')
			print(empID, end = '\t')
			employeeDict[empID].display()

		# Option 3: Change an Employee's Info (Done)

		elif choice == 3:

			opt3 = True

			empID = int(input('\nPlease enter an Employee ID to edit: '))

			while opt3:

				if empID in employeeDict:
					print('\nID', '\tName', '\t\tDepartment', '\tTitle')
					print('---------------------------------------------------------------')
					print(empID, end = '\t')
					employeeDict[empID].display()

					print('1. Name ')
					print('2. Department ')
					print("3. Job Title ")
					print("4. Main Menu\n")
				
					subChoice = int(input('Which would you like to change: '))

					if subChoice == 1:
						tempName = input("\nPlease enter the new Employee's new name: ")
						employeeDict[empID].setName(tempName) 

					elif subChoice == 2:
						tempDepartment = input("\nPlease enter the Employee's new Department: ")
						employeeDict[empID].setDepartment(tempDepartment) 

					elif subChoice == 3:
						tempTitle = input("\nPlease enter the Employee's new Job Title: ")
						employeeDict[empID].setJobTitle(tempTitle) 

					elif subChoice == 4:
						opt3 = False

				else:
					print('\nThere is no Employee with that Employee ID!\n')

		# Option 4: Delete an Employee from the System (Done)

		elif choice == 4:
			empID = int(input('\nPlease enter the Employee ID to Delete: '))

			if empID in employeeDict:
				print('\nID', '\tName', '\t\tDepartment', '\tTitle')
				print('---------------------------------------------------------------')
				print(empID, end = '\t')
				employeeDict[empID].display()
				print(employeeDict[empID].getName(), 'has been deleted from the System!\n')
				del employeeDict[empID]
			else:
				print('\nThere is no Employee with that Employee ID!\n')
		

def Question_1():

	print('\nQuestion 1')
	print('----------')

	program()


"""
Question 2
----------
Code Description: This snippet of code takes in 20 user input numbers and fills a 
				  list, then finds the largest, smallest numbers, the avg, and the sum
				  of all elements in the list.
"""
def findLowest(tempList):
	for j in range(0, len(tempList)):
			smallest = tempList[0]
			for i in range(1, len(tempList)):
				if smallest > tempList[i]:
					smallest = tempList[i]
	return smallest

def findHighest(tempList):
	for j in range(0, len(tempList)):
			largest = tempList[0]
			for i in range(1, len(tempList)):
				if largest < tempList[i]:
					largest = tempList[i]
	return largest

def findSum(tempList):
	sumTotal = 0
	for i in tempList:
		sumTotal += i
	return sumTotal

def findAvg(tempList):
	return findSum(tempList) / len(tempList)


def Question_2():

	print('\nQuestion 2')
	print('----------')

	tempList, newList = [], []
	
	for i in range(0, 20):
		x = int(input("Please enter a number: "))
		newList.append(x)

	tempList = newList

	print("\nThe lowest number in the list is:", findLowest(tempList), end = '\n')

	print("The highest number in the list is:", findHighest(tempList), end = '\n')

	print("The sum of all elements in the list is:", findSum(tempList), end = '\n')

	print("The average of all elements in the list is:", findAvg(tempList), end = '\n')

"""
Question 3
----------
Code Description: This snippet of code generates and prints a dictionary of 
				  size n that contains the numbers (keys) between 1 and n and 
				  the square of each key (values)
"""

def Question_3():

	print('\nQuestion 3')
	print('----------')

	n = -1	# input validation "Do-While" number of elements in the dict is negative

	while n < 1:
		n = int(input("\nEnter the number of elements for a Dictionary: "))

	dictionary_1 = {}	# create the dictionary

	for x in range(1, n+1):		# fill the dictionary with y = x^2
		y = x ** 2
		dictionary_1[x] = y

	print('\n')

	print('Key\tValue')		# display the keys and values
	print('---\t-----')

	for key, value in dictionary_1.items():
		print(key, '\t', value)

	print('\n')	# check to see the last element added into the dictionary
	
	print("Retrieving the most recent addition (", x, "):", dictionary_1[x])	

	print('\n')

	print(dictionary_1.items())	# display everything in the dictionary


"""
Question 4
----------
Code Description: This snippet of code creates a list of a hundred randomly
				  determined values and then gets the second largest number 
				  and removes the repeated elements in the list

"""

def randomNum():
	x = random.randint(0, 20)
	return x

def secondLargest(tempList):
	tempList.remove(max(tempList)) # remove the largest and return the next number
	return max(tempList)

def makeUnique(tempList):
	newList = []

	for i in tempList:
		if i not in tempList:
			newList.append[i]
		
	return newList

def Question_4():
	
	print('\nQuestion 4')
	print('----------')

	newList, uniqueList = [], []

	for i in range(0, 100):
		newList.append(randomNum())

	print('\nThe second largest number in the list is: ', secondLargest(newList.copy()))

	uniqueList = makeUnique(newList.copy())

	for f in uniqueList:
		print(f, end = ' ')

	print('\n')

"""
Main
----
Code Description: Calls all Question methods created in Assignment 4

"""

def main():
	Question_1()
	Question_2()
	Question_3()
	Question_4()

main()

