"""
《内置函数2》
知识点：
1.布尔值bool()
2.

eg.1
>>> 3>2
True
>>> 1<8
True
>>> 3>22
False
>>> True+True
2
>>> type(True)
<class 'bool'>
>>> bool(0)
False
>>> bool(188)
True
>>> bool(-35)
True
>>> bool(True)
True
>>> bool('zyy')
True
>>> bool(None)
False
>>> bool('')
False
>>>

eg.2
>>> while True:
	a=input('请输入你的年龄：')
	if(not bool(a)) or (int(a)<=0):
		print('抱歉，输入有误！')
	else:
		print('您的年龄是:%s'%int(a))

		
请输入你的年龄：3
您的年龄是:3
请输入你的年龄：5
您的年龄是:5
请输入你的年龄：

eg.3
>>> dir(1)
['__abs__',
'__add__',
'__and__',
'__bool__',
'__ceil__',
'__class__',
'__delattr__',
'__dir__',
'__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> 
"""
