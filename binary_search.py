l = [1,2,5,7,8,10,11,88,108,112]

def binary_search(s, l):

	mid = len(l) // 2

	if s == l[mid]:
		return True
	elif len(l) < 2:
		return False
	elif s > l[mid]:
		return binary_search(s, l[mid:])
	elif s < l[mid]:
		return binary_search(s, l[:mid])

print binary_search(11, l)
