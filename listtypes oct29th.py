Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list()
a=[2,4.5,"python",8+9j,True,False]
print(a)
[2, 4.5, 'python', (8+9j), True, False]
type(a)
<class 'list'>
b=4.5
4
4
type(b)
<class 'float'>
c=[4.6]
type(c)
<class 'list'>
a=["python","java","c","c++"]
a.append("ai")
a
['python', 'java', 'c', 'c++', 'ai']
a.append("ml","dsa")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a.append("ml","dsa")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["ml","dsa"])
a
['python', 'java', 'c', 'c++', 'ai', ['ml', 'dsa']]
#extend()
a=["dsa","ai","ml"]
a.extend(["python","java"])
a
['dsa', 'ai', 'ml', 'python', 'java']
#insert()
b=["black","white"]
b.insert(1,"red")
b
['black', 'red', 'white']
a=["apple","mango","kiwi"]
a.index("mango")
1
a.copy()
['apple', 'mango', 'kiwi']
b=a.copy()
b
['apple', 'mango', 'kiwi']
a=["vija","vzag","hyd"]
a.pop()
'hyd'
a
['vija', 'vzag']
a.pop(1)
'vzag'
a.pop("vja")
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a.pop("vja")
TypeError: 'str' object cannot be interpreted as an integer
a
['vija']
a.pop(0)
'vija'
#remove()
a["hi","hello","how"]
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a["hi","hello","how"]
TypeError: list indices must be integers or slices, not tuple
a=["hi","hello","how"]
a.remove("how")
a
['hi', 'hello']
a.remove(1)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    a.remove(1)
ValueError: list.remove(x): x not in list
a=["java","ai","ml"]
a.clear()
a
[]
b.append("pooja")
b
['apple', 'mango', 'kiwi', 'pooja']
a=["banana","graphes","apple","mango","kiwi"]
a.sort()
a
['apple', 'banana', 'graphes', 'kiwi', 'mango']
b=[7,0,2,5,10,8,1]
b.sort()
b
[0, 1, 2, 5, 7, 8, 10]
c=[5+9j,2+4j,6+9j]

c.sort()
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    c.sort()
TypeError: '<' not supported between instances of 'complex' and 'complex'
>>> d=[6,8,9,"gopi","hello",6+9j]
>>> d.sort()
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    d.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
>>> c=[4.5,8.9,2.3]
>>> c.sort()
>>> c
[2.3, 4.5, 8.9]
>>> d=[True,False,True]
>>> d.sort()
>>> d
[False, True, True]
>>> a=["black","red","white"]
>>> a.reverse()
>>> a
['white', 'red', 'black']
>>> b=[5,8,0,1,6,9]
>>> b.reverse()
>>> b
[9, 6, 1, 0, 8, 5]
>>> a=["java","ai","ml"]
>>> len(a)
3
>>> b="java"
>>> len(b)
4
>>> c=["java"]
>>> len(c)
1
>>> a.count("ai")
1
>>> a.count("a")
0
>>> b=["java","ai","a","ml"]
>>> b.count("a")
1
