import random

"""
Question 1
----------
Code Description: This code creates a class called car and uses a series
				  of class method calls to manipulate the cars speed.

Author: Manuel Sebastian Hernandez
Date: February 12th, 2022
""" 
def Question_1():

	class Car:
		"""My car class"""
		def __init__(self, make, yearModel):
			self.make = make
			self.yearModel = yearModel
			self.speed = 0

		def accelerate(self):
			self.speed += 5

		def brake(self):
			self.speed -= 5 

		def get_speed(self):
			return self.speed

	car_1 = Car('Ford', 2019)

	for i in range (0, 5):
		car_1.accelerate()
		print('\nSpeed:', car_1.get_speed(), end = ' ')

	for i in range (0, 5):
		car_1.brake()
		print('\nSpeed:', car_1.get_speed(), end = ' ')

	print('\n')

"""
Question 2
----------
Code Description: This code demonstrates the use of a class called Employee
				  to store information about 3 employees and display them.

"""

def Question_2():

	class Employee:
		"""My Employee Class"""
		def __init__(self, name, IDnumber, department, jobTitle):
			self.name = name
			self.IDnumber = IDnumber
			self.department = department
			self.jobTitle = jobTitle

		def display(self):
			print(self.name, '\t', self.IDnumber, '\t\t', self.department, '\t', self.jobTitle, end = '\n')


	emp_1 = Employee('Susan Meyers', '47899', 'Accounting', 'Vice President')
	emp_2 = Employee('Mark Jones', '39119', 'Manufacturing', 'Engineer')
	emp_3 = Employee('Joy Rogers', '81774', 'IT', '\t Programmer')

	print('\nName', '\t\t', 'ID Number', '\t', 'Department', '\t','Title')
	print('---------------------------------------------------------------')

	emp_1.display()
	emp_2.display()
	emp_3.display()

	print('\n')

"""
Question 3
----------
Code Description: This code demonstrates the use of a class called Employee
				  to store information about an employees and then manipulates
				  the class attributes of his name and email to display according
				  to certain criteria.

"""

def Question_3():
	class Employee_2:

		"""My Employee Class"""
		def __init__(self, fName, lName):
			self.fullName = fName + ' ' + lName
			self.email = fName + '.' + lName +'@company.com' 

		def display(self):
			print('Employee Name:', self.fullName.title(), '\nEmployee Email', self.email.lower(), end = '\n')

	emp_1 = Employee_2('JoSEPh', 'JoEStaR') # create an employee with my name
	emp_1.display() # calls the display method in the employee class

	print('\n')

"""
Question 4
----------
Code Description: This code demonstrates a student class and its member variables
				  that are used to sort the percentages of each student and calculate 
				  the averages of 6 different courses the students are enrolled in. 

"""

def Question_4():

	class Student:

		"""My Student Class"""
		def __init__(self, num, sci, math, read, eng, his, art):
			self.studentNum = num
			self.mathGrade = math
			self.scienceGrade = sci
			self.readingGrade = read
			self.englishGrade = eng
			self.historyGrade = his
			self.artGrade = art
			self.totalPercent = round(((math + sci + read + eng + art + his) / 600) * 100, 2)

	stu_List = []
	sortedList = []

	# a method used to create and return one random number 

	# 50 - 100 range becauses my students aren't dumb lol

	def randomNum():
		x = random.randint(50, 100)
		return x

	# a method used to sort the students in stu_List 

	def sortStudents(startingList):
		newList = []
		smallest = Student(0,0,0,0,0,0,0)

		for j in range(0, len(startingList)):
			smallest = startingList[0]
			temp = 0
			for i in range(1, len(startingList)):
				if smallest.totalPercent > startingList[i].totalPercent:
					smallest = startingList[i]
					temp = i
			newList.append(smallest)
			del startingList[temp]
		return newList

	# a method used to find the averages of the 6 courses

	def findAvg(startingList):
		newList = []

		sumOfSci = 0
		sumOfEng = 0
		sumOfHis = 0
		sumOfMath = 0
		sumOfRead = 0
		sumOfArt = 0

		for i in range(0, len(startingList)):
			sumOfSci += startingList[i].scienceGrade
			sumOfEng += startingList[i].englishGrade
			sumOfHis += startingList[i].historyGrade
			sumOfMath += startingList[i].mathGrade
			sumOfRead += startingList[i].readingGrade
			sumOfArt += startingList[i].artGrade

		newList.append(sumOfSci/25)
		newList.append(sumOfEng/25)
		newList.append(sumOfHis/25)
		newList.append(sumOfMath/25)
		newList.append(sumOfRead/25)
		newList.append(sumOfArt/25)

		return newList


	# create a list of students by initializing students with random values 
	# and then appending them to a list

	studentNames = ['Mike', 'Michael', 'Michelle', 'Marty', 'Mary', 'Mark', 'Marvin', 'Mick', 
					'Anne', 'Annabel', 'Gary', 'Gerald', 'Jesus', 'Kody', 'Sebastian', 'Joe',
					'Thomas', 'James', 'Carlos', 'Logan', 'Kendall', 'Justin', 'Pete', 'Cesar',
					'Ashley']

	

	for i in range(0, 25):
		stu = Student(studentNames[i], randomNum(), randomNum(), randomNum(), randomNum(), randomNum(), randomNum())
		stu_List.append(stu)

	print('Student List (Unsorted)')
	print('-----------------------')
	
	for i in range(0, len(stu_List)):
		print('Student:', stu_List[i].studentNum)
		print('Percentage:', stu_List[i].totalPercent, '\n')

	sortedList = sortStudents(stu_List) # sort method call sends the list

	print('\n\nStudent List (Sorted)')
	print('---------------------')

	for i in range(0, len(sortedList)):
		print('Student:', sortedList[i].studentNum)
		print('Percentage:', sortedList[i].totalPercent, '\n')

	# calculating course averages

	print('\n\nCourse Averages')
	print('---------------')

	courseAverages = findAvg(sortedList)

	courseNames = ['\nScience', 'English', 'History', 'Math', 'Reading', 'Art']

	for i in range(0, 5):
		print(courseNames[i], 'Course Average:', courseAverages[i], '\n')

	print('\n')

"""
Main
----
Code Description: Calls all Question methods created in Assignment 3
"""

def main():
	Question_1()
	Question_2()
	Question_3()
	Question_4()

main()