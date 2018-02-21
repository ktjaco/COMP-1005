from __future__ import division

class A(object):
	def __init__(self,n):
		self.a = n
		
	def total(self):
		return self.a
		
class B(A):
	def __init__(self,n):
		self.b = n
		super(B, self).__init__(n//3 + 2)
		
	def total(self):
		return self.b + super(B,self).total()

class C(B):
	def __init__ (self,n):
		self.c = n
		super(C, self).__init__(2*n+3)
		
	def total(self):
		return self.c + super(C,self).total()
		
C = C(8545).total()
print C
B = B(8545).total()
print B