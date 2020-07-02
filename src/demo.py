import json
from properform import profile, memory_leak

profile.start()
memory_leak.start()

def calc(f, g, a):
	i = 0
	result = []
	while i < len(g):
		result.append((f[a - i] if a >= i and a - i < len(f) else 0) * g[i])
		i += 1
	return sum(result)

def convolution(f, g=[1, 1, 1]):
	i = 0
	result = []
	while i < len(f):
		result.append(calc(f, g, i))
		i += 1
	json.dumps({'result': result}, indent = 4)
	return result

if __name__ == "__main__":
	for _ in range(10000):
		for _ in convolution([1, 2, 3, 4, 5], [1, 1, 1]):
			pass

profile.collect('demo.profile')
memory_leak.collect('demo.memleak')
