from __future__ import division

class Book(object): #creating a class called Books
	def __init__(self,auth,tit,ci,pub,yr): #__init__ method that takes the author, title, city, publisher, and year into consideration
		self.author = auth #self assignments which refers to whatever book your talking about
		self.title = tit #parameter self is needed when defining class methods
		self.city = ci
		self.publisher = pub
		self.year = yr
		
	def mla_string(self): #first function method for the class Book for an MLA string
		return "%s. %s. %s: %s, %d." % (self.author,self.title,self.city,self.publisher,self.year)
		#strings which give the author, title, city, publisher and year in proper MLA format
		
	def apa_string(self): #second function method for the class Book for an APA string
		return "%s. (%s). %s. %s: %d." % (self.author,self.title,self.city,self.publisher,self.year)
		#strings which give the author, title, city, publisher, and year in proper APA format
		
books = [] #creating an empty list then appends 5 different books into the empty list
books.append(Book("John Howat","All About Python","Ottawa","Carleton Press",2014))
books.append(Book("Thomas Lillesand","Remote Sensing and Image Interpretation","New York","John Wiley & Sons, Inc",2008))
books.append(Book("Richard Harris","Statistics for Geography and Environmental Science","London","Pearson Education Limited",2011))
books.append(Book("Margot Northey","Making Sense: Geography and Environmental Sciences","Don Mills","Oxford University Press",2009))
books.append(Book("John Krygier","Making Maps: A Visual Guide to Map Design in GIS","New York","Guilford Press",2011))

print
print books[0].mla_string()	#result: John Howat. All About Python. Ottawa: Carleton Press, 2014.
print						
print books[1].mla_string()	#result: Thomas Lillesand. Remote Sensing and Image Interpretation. New York: John Wiley & Sons, Inc, 2008.
print						
print books[2].mla_string()	#result: Richard Harris. Statistics for Geography and Environmental Science. London: Pearson Education Limited, 2011.
print						
print books[3].mla_string()	#result: Margot Northey. Making Sense: Geography and Environmental Sciences. Don Mills: Oxford University Press, 2009.
print						
print books[4].mla_string()	#result: John Krygier. Making Maps: A Visual Guide to Map Design in GIS. New York: Guilford Press, 2011.

print
print books[0].apa_string()	#result: John Howat. (All About Python). Ottawa. Carleton Press: 2014.
print
print books[1].apa_string() #result: Thomas Lillesand. (Remote Sensing and Image Interpretation). New York. John Wiley & Sons, Inc: 2008.
print
print books[2].apa_string()	#result: Richard Harris. (Statistics for Geography and Environmental Science). London. Pearson Education Limited: 2011.
print
print books[3].apa_string()	#result: Morgot Northey. (Making Sense: Geography and Environmental Sciences). Don Mills. Oxford University Press: 2009.
print
print books[4].apa_string()	#result: John Krygier. (Making Maps: A Visual Guide to Map Design in GIS). New York. Guilford Press: 2011.
print

def books_from_year(books,year): #defining a function that takes a input of a list (books) and a year (year) and return the number of elements in books equal to the year
	e = [] #an empty list which will eventually print the number of elements equal to the year
	for n in books: #for loop which compares a book to the year
		if n.year == year: #if the year of the book is equal to the year in the call of the function
			e.append(n)	#passes an object (n) into an existing list (e)
	return len(e) #counts the number of elements using length of e (empty list)
	
print books_from_year(books,2011) #result: 2
print books_from_year(books,2008) #result: 1




