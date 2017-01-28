# -*- coding: utf-8 -*-

def triangles():
	i,pre = 1,[1,1]
	while True:
		if i == 1:
			yield [1]
		elif i==2:
			yield [1,1]
		else:
			nt = []
			nt.append(1)
			for key,value in enumerate(pre):
				if len(pre)-1 != key:
					nt.append(value + pre[key+1])
			nt.append(1)
			pre = nt
			yield pre
		i += 1

# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break