import re

"""
Question 1
----------
Code Description: This code takes a class called student and fills it with info
				  that is contained in a text file using Regular Expressions.

Author: Manuel Sebastian Hernandez
Date: March 6th, 2022
""" 

def Question_1(): 	

	class Student:

		def __init__(self, firstName, lastName, email, allCourse):
			self.firstName = firstName
			self.lastName = lastName
			self.email = email
			self.allCourse = allCourse

		def setFirstName(self, firstName):
			self.firstName = firstName

		def getFirstName(self):
			return self.firstName

		def setLastName(self, lastName):
			self.lastName = lastName

		def getLastName(self):
			return self.lastName

		def setEmail(self, email):
			self.email = email

		def getEmail(self):
			return self.email

		def setCourses(self, allCourse):
			self.allCourse = allCourse

		def getCourses(self):
			return self.allCourse

	print('\nQuestion 1:')
	print('-----------')

	# Start

	infile = open('students.txt', 'r')

	stringthing = infile.read()

	infile.close()

	find_email = re.findall('[a-z]+@islander.tamucc.edu', stringthing)

	for temp in find_email:
		print(temp)

	# End
	

"""
Question 2
----------
Code Description: Reads through a number of files that is given by the user
				  and finds usable files that are then compiled into one 
				  large file.

"""

def Question_2():
	
	print('\nQuestion 2:') 
	print('-----------') 

	flag = True

	while flag or n < 1:
		try:
			n = int(input("Please enter a number of files to read: "))
			flag = False

		except ValueError:
			print("\nUser entered a char or alpha value instead of an integer!\n")


	flag = True

	finalDraft, count = [], 1

	filePrefix, fileSuffix = 'f', '.txt'

	while flag and count <= n:

		try:

			fileName = filePrefix + str(count) + fileSuffix

			inFile = open(fileName, 'r')

			finalDraft.append(inFile.read())
	
			inFile.close()

			count += 1

		except FileNotFoundError:
			print("\nThe file you are trying to access does not exist!\n")

			count += 1

		except Exception:
			print("\nSomething unexpected went wrong!\n")

			flag = False

	# writing to a file

	inFile = open('final_file.txt', 'w')

	for line in finalDraft:
		inFile.write(line)

	inFile.close()

	# display

	inFile = open('final_file.txt', 'r')

	print(inFile.read())

	print('\n')

	inFile.close()

"""
Main
----
Code Description: Calls all Question methods created in Assignment 6

"""

def main():
	Question_1()
	Question_2()

main()
