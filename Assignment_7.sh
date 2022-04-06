#!/bin/sh

<<com
Name: Manuel Sebastian Hernandez
Date: April 1st, 2022 
com

# Problem 1

echo " "

echo "This is Assignment 7!"

# Problem 2

echo " "

name="Sebastian Hernandez"
Course_1="Probability and Statistics"
Course_2="Introduction to Scripting"
Course_3="Cyber Security"
Course_4="Database Management Systems"

echo "Student Name: $name"
echo "Courses: $Course_1"
echo "         $Course_2"
echo "         $Course_3"
echo "         $Course_4"

echo " "

# Problem 3



# Problem 4

RANDOM=$$

echo $RANDOM
echo " "

echo "Please enter a number:"
read n

echo " "
echo "The number entered was $n"
echo " "

# Problem 5

<<com

RANDOM=$$

R=$(( $RANDOM % 100 + 1 ))

echo $R

A=90
B=80
C=70
D=60

if [[ $R >= $D || $R < $C ]]
then
 echo "Grade: D"
elif [[ $R >= $C || $R < $B ]]
then
 echo "Grade: C"
elif [[ $R >= $B || $R < $A ]]
then
 echo "Grade: B"
elif [ $R >= $A ]
then
 echo "Grade: A"
else
 echo "Grade: Fail"
fi

com

# Problem 6

num1=12
num2=53
num3=9
num4=26
num5=16

echo " 1	2	3	4	5 "
echo " $num1	$num2	$num3	$num4	$num5"
echo " "

SUM=$((num1+num2))
DIF=$((num3-num5))
PRO1=$((num5*num2))
PRO2=$((num4*num3))
DIV=$((num4/num1))

echo "The sum of number 1 and 2 is: $SUM"
echo "The difference of number 3 and 5 is: $DIF"
echo "The product of number 5 and 2 is: $PRO1"
echo "The product of number 4 and 3 is: $PRO2"
echo "The quotient of number 4 and 1 is: $DIV"

echo " "

# Problem 7


