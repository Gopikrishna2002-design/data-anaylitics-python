Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #int()
>>> int(9)
9
>>> int(7.88)
7
>>> int("hi")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int("hi")
ValueError: invalid literal for int() with base 10: 'hi'
>>> int(6+8j)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    int(6+8j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> int(1)
1
>>> int(False)
0
