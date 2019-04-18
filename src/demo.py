def calc(f, g, a):
	i = 0
	result = 0
	while i < len(g):
		if a >= i and a - i < len(f):
			result += f[a - i] * g[i]
		i += 1
	return result

def convolution(f, g):
	return [calc(f, g, i) for i in range(len(f))]

	for _ in xrange(10000):
		for _ in convolution([1, 2, 3, 4, 5], [1, 1, 1]):
			pass