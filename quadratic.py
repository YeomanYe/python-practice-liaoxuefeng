# -*- coding: utf-8 -*-

import math

def quadratic(a, b, c):
	delta = b**2 - 4 * a * c
	return (-b + math.sqrt(delta)) / 2 * a

# 测试:
print(quadratic(2, 3, 1)) # => (-0.5, -1.0)
print(quadratic(1, 3, -4)) # => (1.0, -4.0)