# -*- coding: utf-8 -*-

def is_palindrome(n):
	s = str(n)
	num = int(len(s) / 2)
	if num == 0:
		return False
	while num >= 0 :
		if s[num] != s[-num-1]:
			return False
		num -= 1
	return True


# 测试:
output = filter(is_palindrome, range(1, 1000))
print(list(output))