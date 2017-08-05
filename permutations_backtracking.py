string = 'aabc'

def _get_perms(string, counter, current_perm, perms, level):

	if level == len(string):
		perms.append(current_perm)

	for k, v in counter.items():
		if v > 0:
			counter[k] -= 1
			current_perm[level] = k
			_get_perms(string, counter, current_perm, perms, level + 1)
			counter[k] += 1

	return len(perms)

def get_perms(string):

	counter = {}
	for letter in string:
		if letter not in counter:
			counter[letter] = 1
		else:
			counter[letter] += 1

	current_perm = [0 for i in range(len(string))]

	return _get_perms(string, counter, current_perm, [], 0)

print get_perms(string)
