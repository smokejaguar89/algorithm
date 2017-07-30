l = [5,8,4,3,2,10,100,99,87,58]

def quick_sort(l):

	if len(l) < 2:
		return l
	else:
		pivot = l[0]

		smaller = []
		larger = []

		for x in l:
			if x > pivot:
				larger.append(x)
			elif x < pivot:
				smaller.append(x)

	return quick_sort(smaller) + [pivot] + quick_sort(larger)

print quick_sort(l)
