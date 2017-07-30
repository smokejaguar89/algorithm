a = 'academy'
b = 'abracadabra'

def longest_common_subsequence(a, b):
	matrix = [[0] * (len(b) + 1) for i in range(len(a) + 1)]

	for i, x in enumerate(a):
		for j, y in enumerate(b):
			if x == y:
				matrix[i+1][j+1] = matrix[i][j] + 1
			else:
				matrix[i+1][j+1] = max(matrix[i][j+1], matrix[i+1][j])

	return matrix[len(a)][len(b)]


print longest_common_subsequence(a, b)
