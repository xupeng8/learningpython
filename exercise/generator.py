#!/usr/bin/env python
#! -*- coding:utf-8 -*-

from collections import Iterable, Iterator

# this is not a function, it is a generator
def fib(max):
	n, a, b = 0, 0, 1
	while n < max :
		yield(b)
		n = n + 1
		a, b = b, a+b
	return 'done'

if __name__ == '__main__':
	# this is a list, it was generated when define it.
	L = [ x * x for x in range(1,11) ]
	print(L)

	# this is a generator, the value only generated when you call next on it or iteration it with a for loop.
	g = ( x * x for x in range(1,11) )
	print('g is iterable =', isinstance(g, Iterable))
	print('g is iterator =', isinstance(g, Iterator))
	for n in g:
		print(n, end=',')
	print()

	for n in fib(10):
		print(n, end=',')
	print()
