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
	return result

def convolution(f, g):
	json.dumps({'result': 0}, indent = 4)
	return [calc(f, g, i) for i in range(len(f))]

class test_bound_method_A(object):
	def foo(self):
		pass

def test_bound_method():
	a = test_bound_method_A()
	a.bar = a.foo

def test_mro():
	class A(object):pass
	class B(A):pass
	class C(B):pass

def test_recursive_cellvars():
	def recursive(n):
		if n < 10:
			recursive(n + 1)
	recursive(0)

if __name__ == "__main__":
	for _ in range(10000):
		for _ in convolution([1, 2, 3, 4, 5], [1, 1, 1]):
			pass
	for _ in range(5):
		test_bound_method()
	for _ in range(5):
		test_mro()
	for _ in range(5):
		test_recursive_cellvars()

profile.collect('demo.profile')
memory_leak.collect('demo.memleak')
