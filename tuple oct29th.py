Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #tuple()
>>> a=(6,8,9,"python",2+8j,True,False)
>>> print(a)
(6, 8, 9, 'python', (2+8j), True, False)
>>> type(a)
<class 'tuple'>
>>> a.index(2+8j)
4
>>> a.count(True)
1
>>> len(a)
7
>>> a=4
>>> b=5
>>> print(a*b)
20
>>> print("product is",a*b)
product is 20
>>> print("product is {}".format(a*b))
product is 20
