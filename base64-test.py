# -*- coding: utf-8 -*-

import base64

def safe_base64_decode(s):
	p=len(s)%4
	if p != 0:
		s = s + b'=' * (4-p)
	return (base64.b64decode(s))

# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('Pass')