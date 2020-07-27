import json
from properform import profile, memory_leak

profile.start()
memory_leak.start()

def calc(f, g, a, n, m):
	result = 0
	for i in range(m):
		if a >= i and a - i < n:
			result += f[a - i] * g[i]
	return result

def convolution(f, g ):
	n, m = len(f), len(g)
	json.dumps({'result': n}, indent = 4)
	return [calc(f, g, i, n, m) for i in range(n)]

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
