from __future__ import division

### QUESTION 1 ###

# Fibonacci sequence: 1,1,2,3,5,8...

def fibonacci(n):
	# base cases
	if n == 0: # if n is 0 return 0
		return 0
	elif n == 1: # if n is 1 return 1
		return 1
	else: # else fibo value of (n-2) and add it to the fibo of (n-2)
		  # ie. fibo(5-1) --> 3 .... fibo(5-2) --> 2 (3+2=5)
		return fibonacci(n-1) + fibonacci(n-2)

print "Question 1:"
print fibonacci(1)
print fibonacci(5)
print fibonacci(10)
print

### QUESTION 2 ###

# Tribonacci sequence: 1,1,2,4,7,13,24...

def tribonacci(n):
	a, b, c = 0, 1, 1 # base cases
	for i in range(n):
		# ie. n = 5
		# range(5) -> [0,1,2,3,4].. Tribo 1,1,2,4,7
		# b = 2 and c = 4, a = 1+2+4 = 7
		#return a which is 7 and the tribo value for 5 is 7
		a, b, c = b, c, a + b + c
	return a

print "Question 2:"
print tribonacci(5)
print tribonacci(7)
print tribonacci(10)
print

### QUESTION 3 ###

def multiply(a,b):
	# base cases
	if a == 0: # if a is 0 return 0
			   # ie. multiply(0,4) -> 0*4 = 0
		return 0
	elif a == 1: # if a is 1 return b
				 # ie. multiply(1,9) -> 1*9 = 9
		return b
	else:
		# ie. multiply(2,5)
		# 5 + multiply(2-1, 5)
		# 5 + multiply(1,5)
		# 5 + 5 = 10
		return b + multiply(a-1, b)
		
print "Question 3:"
print multiply(2,5)
print multiply(5,2)
print multiply(5,8)
print multiply(7,9)
print

### QUESTION 4 ###

def exponent(a,b):
	# base cases
	if b == 0: # if b is 1 return 1
		return 1
	else:
		# ie. exponent(2,3)
		# 2 * exponent(2, 3-1)
		# 2 * exponent(2, 2)
		# 2 * 2 * 2 = 8
		return a * exponent(a, b-1)
		
print "Question 4:"
print exponent(2,3)
print exponent(3,2)
print exponent(7,2)
print exponent(5,3)
print

### QUESTION 5 ###

def maximum(a):
	# base cases
	if len(a) == 1: # if the length of a is 1 return the 0th value
		return a[0]
	middle = len(a)//2 # find the middle by splitting
	left = maximum(a[0:middle]) # finding the maximum to the left of the middle
	right = maximum(a[middle:len(a)]) # finding the maximum to the right of the middle
	if left > right: # if the left is greater than the right return the left
		return left
	else: # if not... return the right value
		return right

print "Question 5:"
print maximum(range(10))
print maximum([23,453,124,1232,888])
print maximum(range(10000000))
print