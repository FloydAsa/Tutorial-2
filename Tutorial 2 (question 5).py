# -*- coding: utf-8 -*-
"""
Created on Mon May 08 11:36:51 2017

@author: 214576460
"""

class complex:
	def __init__(self,r=0,c=0):
		self.r=r
		self.i=c
	def copy(self):
		return complex(self.r,self.i)

	def __add__(self,val):
		ans=self.copy()
		if isinstance(val,complex):
			ans.r=ans.r+val.r
			ans.c=ans.i+val.i
		else:
			ans.r=ans.r+val
		return ans

	def __mul__(self,val):
		ans=self.copy()
		if isinstance(val,complex):
			ans.r=self.r*val.r-self.i*val.i
			ans.i=self.r*val.i+self.i*val.r
		else:
			ans.r=ans.r*val
			ans.i=ans.i*val
		return ans

	def __sub__(self,val):
		ans=self.copy()
		if isinstance(val,complex):
			ans.r=ans.r+val.r
			ans.c=ans.i-val.i
		else:
			ans.r=ans.r-val
		return ans

	def __div__(self,val):
		
		if isinstance(val,complex):
			val=val.copy
			val.i=-1*val.i
			ans=self*val
			myabs=val.r**2+val.i**2
			ans=ans*(1.0/myabs)
		else:
			ans=self*(1.0/val)
		return ans

	def __repr__(self):
		if (self.i<0):
			return repr(self.r)+' - '+repr(-1*self.i) +'i'
		else:
			return repr(self.r)+' + '+repr(-1*self.i) +'i'
	
if __name__=="__main__":
	
	k=complex(2.0,5)
	x=complex(1.0,4)
	
	print k+x
	print k-x
	print k*x
print k/5