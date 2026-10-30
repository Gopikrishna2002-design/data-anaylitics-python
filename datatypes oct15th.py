Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatypes
a=10
type(a)
<class 'int'>
b=5.6
type(b)
<class 'float'>
>>> c='python'
>>> type(c)
<class 'str'>
>>> d="codegnan"
>>> type(d)
<class 'str'>
>>> e='''course'''
>>> type(e)
<class 'str'>
>>> f=4+9j
>>> type(f)
<class 'complex'>
>>> g=21+9j
>>> type(g)
<class 'complex'>
>>> x=2j
>>> type(x)
<class 'complex'>
>>> a=2+8i
SyntaxError: invalid decimal literal
>>> b=j
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    b=j
NameError: name 'j' is not defined
>>> c=True
>>> type(c)
<class 'bool'>
>>> b=False
>>> type(b)
<class 'bool'>
