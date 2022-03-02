import random
import math

"""
Question 1
----------
Code Description: This code converts any user input into morse code

Author: Manuel Sebastian Hernandez
Date: February 27th, 2022
""" 

def Question_1(): # Authors Note: I changed the space from ' ' to a '/' as it allows
				  # 			  for better readability.
	
	morseCodeDict = {' ' : '/', '.' : '.-.-.-', ',' : '--..--', '?' : '..--..',
	'1' : '.----', '2' : '..---', '3' : '...--', '4' : '....-', '5' : '.....',
	'6' : '-....', '7' : '--...', '8' : '---..', '9' : '----.', '0' : '-----',
	'a' : '.-', 'b' : '-...', 'c' : '-.-.', 'd' : '-..', 'e' : '.', 'f' : '..-.',
	'g' : '--.', 'h' : '....', 'i' : '..', 'j' : '.---', 'k' : '-.-',
	'l' : '.-..', 'm' : '--', 'n' : '-.', 'o' : '---', 'p' : '.--.',
	'q' : '--.-', 'r' : '.-.', 's' : '...', 't' : '-', 'u' : '..-',
	'v' : '...-', 'w' : '.--', 'x' : '-..-', 'y' : '-.-', 'z' : '--..'
	}

	# check to see if the dictionary is filled correctly

	#for key, value in morseCodeDict.items(): 
		#print(key, value, end = '\n')

	print('\nQuestion 1:') 
	print('-----------') 

	phrase = input("Please enter a phrase to be converted into Morse Code: ")

	print('') 		# this is just a glorified endline

	print('Phrase: ', phrase, end = '\n')

	phrase = phrase.lower()

	print('\nMorse Code: ', end = '')

	for ch in phrase:
		for key, value in morseCodeDict.items(): 
			if ch == key:
				print(value, end = ' ') 

	print('\n\n')

"""
Question 2
----------
Code Description: This snippet of code takes a string from the user and calculates
				  the number of vowels and consonants in the string.

"""

def vowelCount(phrase):
	count = 0

	# print(phrase)

	temp = phrase.lower()

	for ch in temp:
		if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u': 
			count += 1

	return count

def consonantCount(phrase):
	count = 0

	# print(phrase)

	temp = phrase.lower()

	for ch in temp:
		if ch != 'a' and ch != 'e' and ch != 'i' and ch != 'o' and ch != 'u': 
			if ch.isalpha():
				count += 1

	return count

def Question_2():
	
	print('\nQuestion 2:') 
	print('-----------') 

	phrase = input("Please enter a string: ")

	print('\nThe number of vowels in the string is: ', vowelCount(phrase))

	print('\nThe number of consonants in the string is: ', consonantCount(phrase))

	print('\n')

"""
Question 3
----------
Code Description: This code takes 4 pre-determined strings and counts the letters/digits/symbols,
				  removes special symbols, replaces characters, and removes all consonants from
				  a string

"""

def alphaCheck(phrase):
	count = 0
	for ch in phrase:
		if ch.isalpha():
			count += 1
	return count

def digitCheck(phrase):
	count = 0
	for ch in phrase:
		if ch.isdigit():
			count += 1
	return count

def symbolCheck(phrase):
	count = 0
	for ch in phrase:
		if not ch.isalpha() and not ch.isdigit():
			count += 1
	return count

def removeConsonants(phrase):
	tempPhrase = ''

	temp = phrase.lower()

	for ch in temp:
		if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u': 
			tempPhrase = tempPhrase + ch

	return tempPhrase

def Question_3():
	
	print('\nQuestion 3 (Part 1):') 	# Part 1
	print('--------------------') 

	str1 = "P@#yn26at^&i5ve"

	print('The number of letters in ', str1, ' is: ', alphaCheck(str1))

	print('The number of digits in ', str1, ' is: ', digitCheck(str1))

	print('The number of symbols in ', str1, ' is: ', symbolCheck(str1))

	print('\n')			    # Part 2

	str2 = "/*Jon is @developer & musician"

	newStr2 = ''

	for ch in str2:
		if ch.isalpha():
			newStr2 = newStr2 + ch

	print('Question 3 (Part 2) Results: ', newStr2)

	print('\n')				# Part 3

	str3 = "Emma-is-a-data-scientist"

	str3 = str3.replace('-', ' ')

	print('Question 3 (Part 3) Results: ', str3)

	print('\n')				# Part 4

	str4 = "Hello, have a good day"

	str4 = removeConsonants(str4)

	print('Question 3 (Part 4) Results: ', str4)

	print('\n')				

"""
Question 4
----------
Code Description: This code creates a list in range 0 - n (number taken from user)
				  and displays the avg, standard deviation, and mean then creates
				  a new list comprised of the adjacent numbers in the first list
				  divided.
"""

def randomNum():
	x = random.randint(0, 100)
	return x

def findSum(temp):
	sumTotal = 0
	for i in temp:
		sumTotal += i
	return sumTotal

def findAvg(temp):
	return round(findSum(temp) / len(temp), 2)

def findStandDev(newList):
	tempSum = 0
	tempAvg = findAvg(newList)
	for num in newList:
		tempSum += (num - tempAvg) ** 2
	return round(math.sqrt(tempSum / len(newList)), 2)

def sortList(startingList):
		newList = []
		smallest = 0

		for j in range(0, len(startingList)):
			smallest = startingList[0]
			temp = 0
			for i in range(1, len(startingList)):
				if smallest > startingList[i]:
					smallest = startingList[i]
					temp = i
			newList.append(smallest)
			del startingList[temp]
		return newList

def findMedian(newList):
	tempList = sortList(newList)
	# print(tempList)
	if len(tempList) % 2 == 1:
		index = (len(tempList)) // 2
		median = tempList[index]
	else:
		index = (len(tempList)) // 2
		median = (tempList[index-1] + tempList[index]) / 2
	return median

def Question_4():
	
	print('\nQuestion 4 (Part 1):') 
	print('--------------------', end = '') 

	flag = True
	num1 = 0

	while flag or num1 <= 10:
		try:
			num1 = int(input("\nPlease enter a number for a list of integers (n > 10): " ))
			flag = False
		except Exception:
			print("\nPlease enter a number!")

	listPart1 = []

	for i in range(0, num1):
		listPart1.append(randomNum())

	print('\nThe list contains: ', end = '')

	for num in listPart1:
		print(num, end = ' ')

	print('\n')

	print('The average of the list is: ', findAvg(listPart1), end = '\n\n')

	print('The standard deviation of the list is: ', findStandDev(listPart1), end = '\n\n')

	tempList = listPart1.copy()

	print('The median of the list is: ', findMedian(tempList), end = '\n\n')

	# Part 2

	listPart2 = []

	try:
		for i in range(0, len(listPart1)-1):
			listPart2.append(round(listPart1[i]/listPart1[i+1], 2))
			i+2
	except Exception:
		print("Something went wrong! Perhaps, Division by Zero?\n")
	finally:
		print('Part 2 Results: ', listPart2)

	print('\n')			

"""
Question 5
----------
Code Description: This code takes a pre-determined string and manipulates it in a 
				  4 ways: sets the first letter of each word to uppercase, the latter
				  and removes all spaces, converts all 's' to $, and capitalizes only
				  the words This, String, and Class in the phrase only using loops for 
				  all.

"""

def Question_5():
	
	print('\nQuestion 5:') 
	print('-----------') 

	str1 = "this is the string for the class"

	# Part 1

	str1List = str1.split()		

	strTemp = '' 

	for word in str1List:
		strTemp = strTemp + word.title() + ' '

	print(strTemp)

	# Part 2

	strTemp = ''				

	for word in str1List:
		strTemp = strTemp + word.title()

	print(strTemp)

	# Part 3

	strTemp = ''

	strPart3 = ''	

	for word in str1List:
		strTemp = strTemp + word.title() + ' '			

	for ch in strTemp:
		if ch == 's' or ch == 'S':
			strPart3 = strPart3 + '$'
		else:
			strPart3 = strPart3 + ch

	print(strPart3)

	# Part 4

	strTemp = ''				

	for word in str1List:
		strTemp = strTemp + word.title() + ' '

	print(strTemp, end = '\n\n')

"""
Main
----
Code Description: Calls all Question methods created in Assignment 5

"""

def main():
	Question_1()
	Question_2()
	Question_3()
	Question_4()
	Question_5()

main()
