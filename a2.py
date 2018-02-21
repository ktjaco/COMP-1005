##############
# QUESTION 1 #
##############

from __future__ import division

def factorial(n): 	#defining a function that finds the factorial of a positive integer
    if n == 0: 		#if the number is 0 return (print) 1
        return 1
    else: 			#otherwise return n! = (n) * (n-1) * (n-2)..etc
        return n * factorial(n-1) 
					#subtract 1 from n and multiply each time until 1

print factorial(8) #result: 40320
print factorial(0) #result: 5040

##############
# QUESTION 2 #
##############

def add_sum(a, b): 	#defining a function that adds the sum
	return a + b 	#calculator to add a + b
	
def add_list(a): 	#defining a function that adds the sum of a list of numbers
	return reduce(add_sum, a) 
					#reduce("calculator", "list") which uses the add_sum function and a (list)
	
print add_list([3,5,6,10,45])	#result: 69
print add_list([8,4,2,9,50]) 	#result: 73

##############
# QUESTION 3 #
##############

def average(a):				#defining a function which calculates the average of numbers in a list
    total = 0 				#assigning total to be 0
    for n in a: 			#for loop to assign how much the total is
        total = total + n 	#assigning total to add and to n - calculates sum in list a
    return total / len(a) 	#how to calculate the average - len() being the length (how many numbers in a)

print average([2,3]) 		#result: 2.5
print average([10,22,4])	#result: 12.0

##############
# QUESTION 4 #
##############

def threshold(a,x):	#defining a function that takes a list of numbers and returns the value greater than or equal to x 
					#for the numbers in a (list) return those that are greater than or equal to x
	return [n for n in a if n >= x]

print threshold([1,2,3,4,5,6,7,8,9],3) 	#result: [3,4,5,6,7,8,9]
print threshold([43,31,900,10,56],50) 	#result: [900, 56]

##############
# QUESTION 5 #
##############

def bmi_category(bmi): 			#defining a function which takes a bmi number and categorizes it
	if bmi < 18.5: 				#if bmi is less than 18.5 print Underweight
		return "Underweight"
	elif 18.5 <= bmi < 25: 		#if bmi is greater than or equal to 18.5 and less than 25 print Normal
		return "Normal"
	elif 25 <= bmi < 30: 		#if bmi is greater than or equal to 25 and less than 30 print Overweight
		return "Overweight"
	elif bmi >= 30: 			#if bmi is greater than or equal to 30 print Obese
		return "Obese"
		
print bmi_category(24) #result: Normal
print bmi_category(13) #result: Underweight
print bmi_category(27) #result: Overweight
print bmi_category(41) #result: Obese

##############
# QUESTION 6 #
##############

def log2(n):		#defining a function that finds the log base 2 of a number
	a = 0 			#assignment of 0 to a (counter to track divisions)
	while n < 1:	#while loop to check if n is less than 1
					#if true do this while loop, if false do next. ex. log2(8)
		a = a + 1 	#counter to count each division
		n = n * 2 	#multiply and assign for n ex. 0.5 * 2 = 1
	while n >= 2: 	#while loop to check if n is greater than or equal to 2
		a = a + 1 	#counter to count each division
		n = n / 2 	#divide and operator to check if 8/2 is still >= 2
					#it is true so the loop will run again...etc until 2/2 is >= 2/2
					#therefore in total this second while loop ran 3 times (log2(8)) = 3
	return a	 	#finally return (print) the number of times a (number of divisions) went through

print log2(22) 		#result: 4
print log2(8) 		#result: 3
print log2(7)		#result: 2
print log2(180) 	#result: 7


