# Checks whether a set is a sigma algebra
def verify(algebra, universe):
	# Check that the universal set is a member
	if universe not in algebra:
		print("Universal set not found")
		return False
	# Make sure closed under complementation
	for subset in algebra:
		if universe - subset not in algebra:
			print("Set not closed under complementation")
			return False
	# Make sure closed under finite union
	for subset in algebra:
		for osub in algebra:
			if subset != osub and union(subset, osub) not in algebra:
				print("Set not closed under union")
				return False
	return True

# Returns the union of 2 sets
def union(a, b):
	for element in b:
		a.add(element)
	return a