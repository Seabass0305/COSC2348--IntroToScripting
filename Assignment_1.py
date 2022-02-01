"""
Programmer's Note: For this assignment i will be attempting to use a new name 
notation. I am familiar with camelCase but will attempt to use hungarian case.

Question 1
----------
Code Description: This code prompts the user for information and then 
				  displays it to the screen.

Author: Manuel Sebastian Hernandez
Date: January 29th, 2022
""" 

print("\nQuestion 1")
print("----------")

sName = input("Please enter your name: ") 

sAddress = input("Please enter your address: ")

sCity = input("Please enter your city: ")

sState = input("Please enter your state: ")

sPhoneNumber = input("Please enter your phone number: ")

sMajor = input("Please enter your major in college: ")

print("\nYour Information")
print("----------------")
print("Name: ", sName, "\n")
print("Address: ", sAddress, "\n")
print("City: ", sCity, "\n")
print("State: ", sState, "\n")
print("Phone Number: ", sPhoneNumber, "\n")
print("College Major: ", sMajor, "\n")

"""
Question 2
----------
Code Description: This code prompts the user for any number of square feet
				  and then calculates and displays the total number of acres.

Author: Manuel Sebastian Hernandez
Date: January 29th, 2022
""" 

print("\nQuestion 2")
print("----------")

fAcreInFeet = 43560

fAcresGiven = float(input("Please enter a number of square feet in your tract of land: "))

fTotalAcres = fAcresGiven / fAcreInFeet

print("\nThere are ", round(fTotalAcres, 2), " acres in your tract of land.\n")

"""
Question 3
----------
Code Description: This snippet of code takes a set value, the travel speed,
				  and uses this to calculate and display the miles traveled 
				  in given time frames.

Author: Manuel Sebastian Hernandez
Date: January 29th, 2022
""" 

print("\nQuestion 3")
print("----------")

print("A car is traveling at 70 mph.\n")

iTravelSpeed = 70

iSixHoursTraveled = 6 * iTravelSpeed
iTenHoursTraveled = 10 * iTravelSpeed
iFifteenHoursTraveled = 15 * iTravelSpeed

print("  I. In 6 hours the car travels ", iSixHoursTraveled, " miles.")
print(" II. In 10 hours the car travels ", iTenHoursTraveled, " miles.")
print("III. In 15 hours the car travels ", iFifteenHoursTraveled, " miles.\n")

"""
Question 4
----------
Code Description: This snippet of code asks for the user's age and then
				  classifies them using an age range guideline

Author: Manuel Sebastian Hernandez
Date: January 29th, 2022
""" 

print("\nQuestion 4")
print("----------")

# I miss do-while loops but this is an easy work around

iUserAge = 0

while iUserAge < 1:
	iUserAge = int(input("Please enter your current age: "))

if iUserAge <= 1:
	print("\nYou are an infant.\n")

elif iUserAge > 1 and iUserAge < 13:
	print("\nYou are a child.\n")

elif iUserAge >= 13 and iUserAge < 20:
	print("\nYou are a teenager.\n")

else:
	print("\nYou are an adult.\n")

"""
Question 5
----------
Code Description: This snippet of code is a game that asks the user for any number
				  of 4 types of coins in an attempt to add them equal to exactly 
				  one dollar's worth of change. 
				  If done correctly, a congratulation screen is then displayed!

Author: Manuel Sebastian Hernandez
Date: January 29th, 2022
""" 

print("\nQuestion 5")
print("----------")

print("\nChange Counting Game!")
print("\nRules: Try to get exacly one dollar using only pennies, nickels, dimes, and quarters\n")

iPennies = 0
iNickels = 0
iDimes = 0
iQuarters = 0

while iPennies < 1:
	iPennies = int(input("Please enter any number of pennies: "))

while iNickels < 1:
	iNickels = int(input("Please enter any number of nickels: "))

while iDimes < 1:
	iDimes = int(input("Please enter any number of dimes: "))

while iQuarters < 1:
	iQuarters = int(input("Please enter any number of quarters: "))

iSumOfCoins = (iPennies * 1) + (iNickels * 5) + (iDimes * 10) + (iQuarters * 25)

if iSumOfCoins < 100:
	print("\nUh Oh! You seem to have gone under one dollar's worth of change, Try Again!\n")

elif iSumOfCoins > 100:
	print("\nUh Oh! You seem to have gone over one dollar's worth of change, Try Again!\n")

elif iSumOfCoins == 100:
	print("\nCongratulations!!! You made exactly one dollar's worth of change!\n")

"""
Question 6
----------
Code Description: This snippet of code asks the user for a year and determines
				  whether or not it is a leap year based on criteria

Author: Manuel Sebastian Hernandez
Date: January 29th, 2022
""" 

print("\nQuestion 6")
print("----------")

fYear = float(input("Please enter a year: "))

if not fYear % 100 and not fYear % 400:
	print("\nThat year is a leap year!\n")

else:
	if not fYear % 4:
		print("\nThat year is a leap year!\n")
	else:
		print("\nThat year is not a leap year!\n")

"""
Question 7
----------
Code Description: This snippet of code works as a BMI calculator.
				  It takes in user data such as weight and height
				  and calculates the users Body Mass Index then 
				  determines if they are below or over their healthy
				  body weight.

Author: Manuel Sebastian Hernandez
Date: January 30th, 2022
""" 

print("\nQuestion 7")
print("----------")

fUserHeight = 0.0
fUserWeight = 0.0

while fUserHeight < 1:	
	fUserHeight = int(input("Please enter your current height in inches: "))

while fUserWeight < 1:	
	fUserWeight = int(input("Please enter your current weight in pounds: "))

fBMI = (fUserWeight / fUserHeight ** 2) * 703

if fBMI < 18.5:
	print("\nBMI: ", round(fBMI, 2), "\nYou are underweight.\n")

elif fBMI > 25:
	print("\nBMI: ", round(fBMI, 2), "\nYou are overweight.\n")

else: 
	print("\nBMI: ", round(fBMI, 2), "\nYou have a healthy BMI.\n")


"""
Question 8
----------
Code Description: This snippet of code calculates the amount of money a man named
				  Joe paid for stock and calculates his loses and gains.

Author: Manuel Sebastian Hernandez
Date: January 31st, 2022
""" 

print("\nQuestion 8")
print("----------")

fStockPrice = 40.00

fJoesMoneyPaid = fStockPrice * 2000.00

print("Joe paid a total of $",fJoesMoneyPaid, " for the Acme Software Stock.\n")

fCommission = fJoesMoneyPaid * 0.03

fJoesMoneyPaid = fJoesMoneyPaid + fCommission

print("Joe paid his broker a total of $",fCommission, " for buying his Stock.\n")

fStockPrice = 42.75

fJoesGain = fStockPrice * 2000.00

print("Joe sold his stock for $",fJoesGain, "\n")

fCommission = fJoesGain * 0.03

print("Joe paid his broker again a total of $", fCommission, " for selling his Stock.\n")

fJoesMoneyPaid = fJoesMoneyPaid + fCommission

fJoesFinalMoney = fJoesGain - fJoesMoneyPaid

if fJoesFinalMoney > 0:
	print("Joe made a profit of $",fJoesFinalMoney, "\n")

elif fJoesFinalMoney < 0:
	print("Joe lost a total of $",fJoesFinalMoney, "\n")



