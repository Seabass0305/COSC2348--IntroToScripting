#!/bin/sh

<<com
Name: Manuel Sebastian Hernandez
Date: April 17th, 2022
com

# Question 1
<<com
Desc: Creates an array of size 20 and uses random to generate the elements, then
      sorts them from lowest number to higher number using a for loop.
com

echo
echo "Question 1"
echo "----------"

declare -a q1Array

for i in {0..19}
do
        q1Array[i]=$(( $RANDOM % 10 + 1  ))
done

# echo "Random Array (Q1): " ${q1Array[@]}

# Begin sort: low to high

declare -a sortedArray	# new sorted array
smallest=0
count=0

for i in {0..19}
do
	smallest=q1Array[0]
	temp=0
	for j in {1, 19}
	do
		if [ $smallest>q1Array[$j] ]
		then
			smallest=q1Array[$j]
			temp=$j
		else
			smallest=q1Array[0]
		fi
	done	
	sortedArray+=( "$smallest" )
	unset q1Array[$temp]
	let count++	
done

echo "Sorted Array (Q1): " "${sortedArray[@]}"

# Question 2
<<com
Desc: Creates an array of size 20 and uses random to generate the elements, then
      sorts them from highest to lowest number using a for loop.
com

echo
echo "Question 2"
echo "----------"

declare -a q2Array

for i in {0..19}
do
	q2Array[i]=$(( $RANDOM % 10 + 1  ))
done

echo "Random Array (Q2): ${q2Array[@]}"

# Begin sort: high to low




# Question 3 (Finished)
<<com
Desc: Creates an array for numbers 1 to 50.
com

echo
echo "Question 3"
echo "----------"

declare -a q3Array
q3Array=( $(seq 1 1 50) )

echo "Array (1-50): ${q3Array[@]}"


# Question 4
<<com
Desc: Using function/method, find the prime numbers from 1 to 50, then using a function/
      -method find the summation of the prime numbers.
com

<<com

echo
echo "Question 4"
echo "----------"

question_4(){
	declare -a primeArray
	arr=$1
	minimum=1
	maximum=50
	count=0

	while [ $minimum<=$maximum ]
	do
		flag=1
		for i in {2..$minimum}
		do
			if [ $minimum%i==0 ]
			then
				flag=0
			fi
		if [ flag ]
		then
			primeArray[count]=$minimum
		fi
		Let minimum+=1
	done
	return primeArray
}

summation(){
	arr=$1
	sum=0
	len=${#arr}

	for i in {0..len}
	do
        	let sum+=arr[i]
	done

	return sum
}

pArray=question_4() q3Array
sum=summation() pArray

echo "Sum of the prime list: " $sum

com

# Question 5 (Finished)
<<com
Desc: 1. Creates an array for odd number from 1 to 50 and finds its summation. 
      2. Creates an array for even numbers from 1 to 50 and finds its summation.
com

echo
echo "Question 5"
echo "----------"

declare -a EVEN_ARRAY
declare -a ODD_ARRAY

ODD_ARRAY=( $(seq 1 2 50) )
EVEN_ARRAY=( $(seq 2 2 50) )

echo "Even Array: ${EVEN_ARRAY[@]}"
echo "Odd Array: ${ODD_ARRAY[@]}"

sumEven=0
sumOdd=0

for i in {0..24}
do
	let sumEven+=EVEN_ARRAY[i]	
	let sumOdd+=ODD_ARRAY[i]
done

echo
echo "Summation of the Even Array: $sumEven"
echo "Summation of the Odd Array: $sumOdd"
echo
