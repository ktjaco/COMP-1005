from __future__ import division

##############
# QUESTION 1 #
##############

def unique(a): #defining a function that takes a list of numbers and returns a new list with each element once
	s = set(a) #assign s to the set of list a
	b = set() #assign b to a new empty set object
	c = [] #assign an empty list which will be returned
	for x in a: #for elements in list a..
		if x in s and x not in b: #if element in set s and element not in set b
			b.add(x) #add element to b
			c.append(x) #append element to the end of empty list c
	return c #return the list of elements that were then stored in c
	
print unique([1,1,2,3,2])
#result: [1, 2, 3]
print unique([2,1,3,1,4])
#result: [2, 1, 3, 4]

##############
# QUESTION 2 #
##############

def pos_and_neg(a): #defining a function which returns a list of numbers and returns a new list that contains each pos. and neg. elements
	s = set(a) #assign s to the set of list a
	b = set() #assign b to a new empty set object
	c = [] #assign an empty list which will be returned
	for x in a: #for elements in list a...
		if -x in s and x not in b: #if neg. element in set s and x not in set b
			b.add(x) #add element to set b
			c.append(x) #append element to the end of empty list c
	return c #return the list of elements that were then stored in c
	
print pos_and_neg([1,2,3,-1,-3])
#result [1, 3, -1, -3]
print pos_and_neg([-1,-2,3,1,2])
#result: [-1,-2,1,2]

##############
# QUESTION 3 #
##############
def encrypt (s,d): #defining a function that takes a string and a dictionary and returns an encrypted version of the string
	mystring = "" #the initial empty string
	for i in s: #for element in the string
		#add and assign mystring to element in d if element is in d else print ?
		mystring = mystring + d[i] if i in d else "?"
	return mystring #return mystring and its encrypted values

d = { 'a' : 'm', 'b' : 'd', 'c' : 'l', 'd' : 'x', 'e' : 'j', 'f' : 't', 'g' : 'u', 'h' : 'k', 'i' : 'z', 'j' : 'd', 'k' : 'o', 'l' : 'y', 'm' : 'i', 'n' : 'v', 'o' : 'p', 'p' : 'q', 'q' : 'f', 'r' : 'c', 's' : 'r', 't' : 'b', 'u' : 'j', 'v' : 'w', 'w' : 'n', 'x' : 'h', 'y' : 's', 'z' : 'a' }

print encrypt('hello', d)
#result: kjyyp
print encrypt('Hello', d)
#result: ?jyyp