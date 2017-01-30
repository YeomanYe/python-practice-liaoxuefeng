# -*- coding: utf-8 -*-

import re
e1 = 'someone@gmail.com'
e2 = 'bill.gates@microsoft.com'
e3 = 'tom@voyager.org'
re_email1 = re.compile(r'([\S\d]*)@[\w\d]*.[\w]*')
print(re_email1.match(e1).group(0))
print(re_email1.match(e2).group(0))
print(re_email1.match(e3).group(1))