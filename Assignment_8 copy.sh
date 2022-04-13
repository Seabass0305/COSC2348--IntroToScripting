#!/bin/sh

<<com
Name: Manuel Sebastian Hernandez
Date: April 10th 2022
Description: This snippet shows how to print the number 1 - 15 using
	     only while, for, and until.
com

# Question 1 (While Loop)

echo ""

echo "Q1 - Part 1"
echo "-----------"

i=1
while (( $i< 16 ))
do
	echo $i
	let i++
done

echo ""

# Question 1 (Until)

echo "Q1 - Part 2"
echo "-----------"

i=1
until [ $i -eq 16 ]
do
	echo $i
	let i++
done

echo ""

# Question 1 (For Loop)

echo "Q1 - Part 3"
echo "-----------"

for n in {1..15}
do
	echo $n
done

echo ""

<<com
Description: This snippet shows how to find the summation of all numbers 20 - 40 using
             only while, for, and until.
com

# Question 2 (While Loop)

echo "Q2 - Part 1"
echo "-----------"

sum=0
count=20
while (( $count <= 40 ))
do 
	let sum+=count
	let count++
done
echo "Summation (While): $sum"

echo ""

# Question 2 (Until)

echo "Q2 - Part 2"
echo "-----------"

sum2=0
count2=20
until [ $count2 -eq 41 ]
do
	let sum2+=count2
	let count2++
done
echo "Summation (Until): $sum2"


echo ""

# Question 2 (For Loop)

echo "Q2 - Part 3"
echo "-----------"

sum3=0
for n in {20..40}
do
      let sum3+=n  
done
echo "Summation (For): $sum3"

echo ""

<<com
Description: This snippet shows how to find the prime numbers less than 50 using
             only while, for, and until.
com

# Question 3 (While Loop)

echo "Q3 - Part 1"
echo "-----------"



echo ""

# Question 3 (Until)

echo "Q3 - Part 2"
echo "-----------"

echo ""

# Question 3 (For Loop)

echo "Q3 - Part 3"
echo "-----------"

<<com

for j in {2..50}
do
	for (( i=2; i<=j/2; i++ ))
	do
		if [ $((num%i)) -eq 0 ]
		then 
			break
		else
			echo $j
			break
		fi
	done	
done

com

echo ""

<<com
Description: Take a input from users, if the user provides “corpus” print “Texas A&M University"	     
com

echo "Question 4"
echo "-----------"

echo "Options: - corpus, kingsville, commerce"

echo ""

echo "Please enter a Texas A&M University Campus:" 
read collegeCity

echo ""

case "$collegeCity" in
   "corpus") echo "Texas A&M University Corpus Christi" 
   ;;
   "kingsville") echo "Texas A&M University Kingsville"
   ;;
   "commerce") echo "Texas A&M University Commerce" 
   ;;
   *) echo "Texas A&M University"
   ;;
esac

echo ""

<<com
Description: I corrected the code to be non equivalent less than or greater than operations.
	     Correct the code to work as intended; To correctly categorize var_test.
com

echo "Bonus Question"
echo "--------------"

var_test=26

if [[ $var_test>0 && $var_test<11 ]]
then
	echo "Between 1 and 10"
elif [[ $var_test>10 && $var_test<21 ]]
then
	echo "Between 11 and 20"
elif [ $var_test>20 ]
then
	echo "Greater than 20"
else
	echo "Less than 1"
fi

echo ""
