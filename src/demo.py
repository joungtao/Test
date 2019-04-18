def calc(f, g, a, n, m):
	result = 0
	for i in xrange(m):
		if a >= i and a - i < n:
			result += f[a - i] * g[i]
	return result

def convolution(f, g ):
	n, m = len(f), len(g)
	return [calc(f, g, i, n, m) for i in xrange(n)]

if __name__ == "__main__":
	for _ in xrange(10000):
		for _ in convolution([1, 2, 3, 4, 5], [1, 1, 1]):
			pass
