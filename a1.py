##############
# QUESTION 1 #
##############

from __future__ import division

def f2c(t): # defining fahrenheit to celsius function; parameter t = temperature in fahrenheit 

	return (t - 32.0) * 5.0 / 9.0 # formula which converts temp in fahrenheit to celsius
	
print f2c(30), "degrees Celsius" # result: -1.11111111111 degrees Celsius

print f2c(80), "degrees Celsius" # result: 26.6666666667 degrees Celsius

print f2c(54), "degrees Celsius" # result: 12.2222222222 degrees Celsius

##############
# QUESTION 2 #
##############

def lboz2kg(p, o): # lbs oz to kg function; parameter p = lbs, o = ounces

	return ((o / 16) + p) * 0.45359237 # formula which converts lb oz to kg
	
print lboz2kg(3,5),"kg" # result: 1.50252472563 kg

print lboz2kg(6,0),"kg" # result: 2.72155422 kg

print lboz2kg(0,3),"kg" # result: 0.085048569375 kg

##############
# QUESTION 3 #
##############

def in2ftin(h): # function which converts inches to ft & inches

	return (int(h / 12), h % 12) # calculates the ft and inches (remainder, %)

(ft,inches) = in2ftin(70) # print in the format _ft _inches

print ft, "ft", inches, "inches" # result: 5 ft 10 inches

(ft,inches) = in2ftin(84) # print in the format _ft _inches

print ft, "ft", inches, "inches" # result: 7 ft 0 inches

(ft,inches) = in2ftin(34) # print in the format _ft _inches

print ft, "ft", inches, "inches" # result: 2 ft 10 inches

##############
# QUESTION 4 #
##############

def bibformat_mla(author,title,city,publisher,year): # defining a function for bibliography in mla format

	return "%s. %s. %s: %s, %s" % (author,title,city,publisher,year) # strings which give the format Author. Title. City: Publisher, Year

print bibformat_mla("John Howat","All About Python","Ottawa","Carleton Press","2014")
# result: John Howat. All About Python. Ottawa: Carleton Press, 2014

print bibformat_mla("Thomas Lillesand", "Remote Sensing and Image Interpretation", "New York", "John Wiley & Sons, Inc", "2008")
# result: Thomas Lillesand. Remote Sensing and Image Interpretation. New York: John Wiley & Sons Inc., 2008.

print bibformat_mla("Richard Harris", "Statistics for Geography and Environmental Science", "London", "Pearson Education Limited", "2011")
# result: Richard Harris. Statistics for Geography and Environmental Science. London: Pearson Education Limited, 2011.

##############
# QUESTION 5 #
##############

def bibformat_apa(author,title,city,publisher,year): # defining a function for bibliography in apa

	return "%s. (%s). %s. %s: %s." % (author,year,title,city,publisher) # strings which give the format Author. (Year). Title. City: Publisher

print bibformat_apa("John Howat","All About Python","Ottawa","Carleton Press","2014")
# result: John Howat. (2014). All About Python. Ottawa: Carleton Press

print bibformat_apa("Thomas Lillesand", "Remote Sensing and Image Interpretation", "New York", "John Wiley & Sons, Inc", "2008")
# result: Thomas Lillesand. (2008). Remote Sensing and Image Interpretation. New York: John Wiley & Sons Inc.

print bibformat_apa("Richard Harris", "Statistics for Geography and Environmental Science", "London", "Pearson Education Limited", "2011")
# result: Richard Harris. (2011). Statistics for Geography and Environmental Science. London: Pearson Eduction Limited.

##############
# QUESTION 6 #
##############

def bmi(w, h): # defining a function which calculates Body Mass Index

	return ( w / ( h * h) ) * 703 # formula which calculates BMI using weight (w) and height (h)
	
print bmi(180, 70) # result: 25.82444897959

print bmi(205, 80) # result: 22.51796875

print bmi(175, 65) # result: 29.1183431953

##############
# QUESTION 7 #
##############

def bmi_calculator(): # defining a BMI calculator

	first_name = raw_input("Enter First Name: ") # Enter First Name:

	last_name = raw_input("Enter Last Name: ") # Enter Last Name:

	w = float(raw_input("Enter Weight (lbs): ")) # Enter Weight (lbs):

	h = float(raw_input("Enter Height (inches): ")) # Enter Height (inches):
	
	bmi = ( w / ( h * h ) ) * 703 # formula which calculates BMI
	
	print "%s %s's BMI is %s" % (first_name, last_name, bmi)
	# print function [somebody]'s BMI is [something]

bmi_calculator() # call the function that was defined (bmi_calculator())

# Example input 1:
# Enter First Name: Kent
# Enter Last Name: Jacobs
# Enter Weight (lbs): 180
# Enter Height (inches): 70
# Kent Jacobs's BMI is 25.82444897959

# Example input 2:
# Enter First Name: Sidney
# Enter Last Name: Crosby
# Enter Weight (lbs): 200
# Enter Height (inches): 71
# Sidney Crosby's BMI is 27.8912914104

# Example input 3:
# Enter First Name: Alex
# Enter Last Name: Johnson
# Enter Weight (lbs): 176
# Enter Height (inches): 79
# Alex Johnson's BMI is 19.8250280404