import json
from properform import profile, memory_leak

profile.start()
memory_leak.start()

def calc(f, g, a, n, m):
	result = 0
	for i in range(m):
		if a >= i and a - i < n:
			result += f[a - i] * g[i]
	json.dumps({'result': result}, indent = 4)
	return result

def convolution(f, g ):
	n, m = len(f), len(g)
	return [calc(f, g, i, n, m) for i in range(n)]

if __name__ == "__main__":
	for _ in range(10000):
		for _ in convolution([1, 2, 3, 4, 5], [1, 1, 1]):
			pass

profile.collect('demo.profile')
memory_leak.collect('demo.memleak')
