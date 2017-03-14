## This constructor class can be used to create a sigma algebra
## You start with the simplest possible sigma algebra: {null, U}
## Then, add some subsets that you wish to be part of the algebra
## Finally, the constructor fixes any errors based on the provided data
## (c) Copyright 2017 Vincent Fiestada <vffiestada@gmail.com>

import verify # See verify.py

class constructor:
	def __init__(self, universe):
		self.universe = frozenset(universe) # Store the universal set U
		self.algebra = set([ frozenset(), self.universe ]) # start with {null, U}
	def add(self, x): # Add a subset
		# Make sure elements of x are in universe
		if (x <= self.universe):
			self.algebra.add(frozenset((e for e in x)))
		else:
			print("Cannot add as ",x,"is not a subset of U")
	def sigmafy(self): # Add necessary members to make sigma algebra
		print("Making sure complements are members...")
		# Make sure it's closed under complementation
		toAdd = set() # This will contain all elements to be added at the end
		for subset in self.algebra:
			complement = self.universe - subset
			toAdd.add(complement)
		for n in toAdd:
			self.algebra.add(n)
		# Make sure it's closed under union
		# Iteratively add unions of sets in the algebra
		oldLen = len(self.algebra)
		toAdd.clear()
		while (True):
			print("Adding unions...")
			for a in self.algebra:
				others = (b for b in self.algebra if b != a)
				for b in others:
					ab = a.union(b)
					toAdd.add(ab) # Add A Union B
					toAdd.add(self.universe - ab) # Add complement of A Union B
			for n in toAdd:
				self.algebra.add(n)
			newLen = len(self.algebra)
			if (newLen == oldLen): # Check if something new has been added
				print("No new unions added. Exiting loop...")
				break
			else:
				oldLen = newLen
		print (self.algebra)
	def getElements(self): # Get elements
		return self.algebra
	def getUniverse(self): # Get universal set
		return self.universe
	def verify(self):
		return verify.verify([set(x) for x in self.algebra], self.universe)
	def pretty(self): # Returns a neater representation
		return list(list(m) for m in self.algebra)

# Sample usage:
# ---------------------------------------
# builder = constructor([1, 2, 3, 4, 5])
# builder.add(set([1]))
# builder.add(set([2,5]))
# builder.sigmafy()
# print("\n\n",
#        builder.pretty(),
# 	  "\n\n")