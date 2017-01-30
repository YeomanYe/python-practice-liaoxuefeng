# -*- coding: utf-8 -*-

class Screen(object):
	@property
	def width(self):
		return self.__width

	@width.setter
	def width(self,value):
		if not isinstance(value,int):
			raise ValueError('width must be an integer!')
		elif value < 0:
			raise ValueError('value must be greatter than 0')
		self.__width = value
		if hasattr(self,'height'):
			self._resolution = self.__width * self.__height

	@property
	def height(self):
		return self.__height

	@height.setter
	def height(self,value):
		if not isinstance(value,int):
			raise ValueError('height must be an integer!')
		elif value < 0:
			raise ValueError('value must be greatter than 0')
		self.__height = value
		if hasattr(self,'width'):
			self._resolution = self.__width * self.__height

	@property
	def resolution(self):
		# self._resolution = self.__height * self.__width
		return self._resolution

# test:
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution