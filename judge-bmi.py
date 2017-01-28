# -*- coding: utf-8 -*-

height = 1.74
weight = 60

bmi = weight / (height * height)
if bmi < 18.55:
	print("过轻")
elif bmi < 25:
	print("正常")
elif bmi < 28:
	print("过重")
elif bmi < 32:
	print("肥胖")
else :
	print("严重肥胖")