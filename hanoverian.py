# -*- coding: utf-8 -*-
num = int(input("Please input a number greater than 0\n"))
def move(n, a, b, c):
	if n != 0:
		move(n-1,a,c,b)
		print('%s --> %s' % (a,c))
		move(n-1,b,a,c)

move(num,'a','b','c')