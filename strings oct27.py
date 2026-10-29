Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string methods
#upper ()
a="code"
a.upper()
'CODE'
b="python"
b.upper()
'PYTHON'
#lower()
c="HELLO"
c.lower()
'hello'
a="python'
SyntaxError: unterminated string literal (detected at line 1)
a="python"
a.capitalize()
'Python'
b="python course"
b.title()
'Python Course'
c="i am in class"
c.capitalize()
'I am in class'
d="i am going to codegnan"
d.title()
'I Am Going To Codegnan'
a="hello"
a.isupper()
False
b="hello gopi"
b.isalpha()
False
b="hellogopi"
b.isalpha()
True
a.isdigit()
False
c="12345"
c.isdigit()
True
a="python course"
a.starswith("p")
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a.starswith("p")
AttributeError: 'str' object has no attribute 'starswith'. Did you mean: 'startswith'?
a="python course"
a.startswith("p")
True
a.endswith("e")
True
b="Python COURSE")
SyntaxError: unmatched ')'
b="Python COURSE"
b.isupper()
False
c="pooja123"
c.isalnam()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    c.isalnam()
AttributeError: 'str' object has no attribute 'isalnam'. Did you mean: 'isalnum'?
#strip()
#rstrip(),lstrip()
a="     gopi       "
a.strip()
'gopi'
a.rstrip()
'     gopi'
a.lstrip()
'gopi       '
#split()
a="python java c c++"
a.split()
['python', 'java', 'c', 'c++']
b="i am learning data anaylitcs"
b.split()
['i', 'am', 'learning', 'data', 'anaylitcs']
c=b.split()

c
['i', 'am', 'learning', 'data', 'anaylitcs']
c[l].upper()
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    c[l].upper()
NameError: name 'l' is not defined

#join()
a="apple","banana","grapes"
"".join(a)
'applebananagrapes'
" ".join(a)
'apple banana grapes'
"k".join(a)
'applekbananakgrapes'
b="hello"
"k".join(b)
'hkeklklko'
#concatenation()
a="code"
b="gnan"
print(a+b)
codegnan

a="python"
b="data"
print(a+b)
pythondata
fname="gopi"
lnane="mavidala"
print(fname+lname)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    print(fname+lname)
NameError: name 'lname' is not defined. Did you mean: 'fname'?
fname="gopi"
lname="mavidala"
print(fname+lname)
gopimavidala
print(fname+" "+lname)
gopi mavidala
print(fname.title()+" "+lname.title())
Gopi Mavidala
>>> print(fname+" "+lname).title())
SyntaxError: unmatched ')'
>>> print((fname+" "+lname)title())
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print((fname+" "+lname).title())
Gopi Mavidala
>>> #formatting
>>> a=5
>>> b=8
>>> print(a+b)
13
>>> print("the sum is",a+b)
the sum is 13
>>> print("the sum is a+b")
the sum is a+b
>>> #format()
>>> a="motu"
>>> b="pathlu"
>>> print("hello {}{}.format(a,b))
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print("hello {}{}".format(a,b))
...       
hello motupathlu
>>> print("hello {} {}".format(a,b))
...       
hello motu pathlu
>>> #fstring
...       
>>> #fstring
...       
>>> 
>>> a="sweety"
...       
>>> b="cutie"
...       
>>> print(f"hello {a}{b}")
...       
hello sweetycutie
>>> print(f"hello {a} {b}")
      
hello sweety cutie
print(f"hello {a} hello {b}")
      
hello sweety hello cutie
a=4
      
b=5
      
#fstring
      
print(f"the multiplication {a}{b}")
      
the multiplication 45
