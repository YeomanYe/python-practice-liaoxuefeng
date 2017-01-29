# -*- coding: utf-8 -*-

from functools import reduce

def str2float(s):
	return reduce(lambda x,y:x * 10 + y,map(int,s[:s.index('.')])) + reduce(lambda x,y:x * 0.1 + y,map(int,s[:s.index('.'):-1])) * 0.1

print('str2float(\'123.456\') =', str2float('123.456'))