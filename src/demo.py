import json
from properform import profile, memory_leak

profile.start()
memory_leak.start()

def calc(f, g, a):
	i = 0
	result = 0
	while i < len(g):
		if a >= i and a - i < len(f):
			result += f[a - i] * g[i]
		i += 1
	json.dumps({'result': result}, indent = 4)
	json.dumps({'result': result}, indent = 4)
	return result

def convolution(f, g):
	return [calc(f, g, i) for i in range(len(f))]

if __name__ == "__main__":
	for _ in range(10000):
		for _ in convolution([1, 2, 3, 4, 5], [1, 1, 1]):
			pass

profile.collect('demo.profile')
memory_leak.collect('demo.memleak')
