Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#add()
a={3,6,7,"python",7+9j,True,False}
print(a)
{False, True, (7+9j), 3, 6, 7, 'python'}
type(a)
<class 'set'>
b={5,7,9,10,12,14,15,10,5}
type(b)
<class 'set'>
print(b)
{5, 7, 9, 10, 12, 14, 15}
a={4,5,6,7,8,9}
a.add(10)
a
{4, 5, 6, 7, 8, 9, 10}
#issubset()
a={1,2,3,4,5,6}
b={4,5,6}
b.issubset(a)
True
a.issubset(b)
False
#superset()
a={2,3,4,5,6,7,8,9}
b={6,7,8,9}
a.issuperset(b)
True
b.issuperset(a)
False
#union()
a={5,6,7,8,9,10}
b={6,7,8,9,10,11,12}
a.union(b)
{5, 6, 7, 8, 9, 10, 11, 12}
#intersection()
a={4,5,6,7,8,9,}
b={7,8,9,10,11,12}
a.intersection(b)
{8, 9, 7}
#update()
a={4,5,6,7,8,9}
b={7,8,9,10,11,12}
a.update(b)
a
{4, 5, 6, 7, 8, 9, 10, 11, 12}
b
{7, 8, 9, 10, 11, 12}
b.update(a)
b
{4, 5, 6, 7, 8, 9, 10, 11, 12}
#difference()
a={3,4,5,6,7,8}
b={8,9,10,11,12}
a.difference(b)
{3, 4, 5, 6, 7}
b.difference(a)
{9, 10, 11, 12}
a={1,2,3,4,5,6}
b={7,8,9,10,11,12}
b.difference(a)
{7, 8, 9, 10, 11, 12}
a.difference(b)
{1, 2, 3, 4, 5, 6}
#symmetric_difference()
a={10,11,12,13,14,15}
b={13,14,15,16,17,18}
a.symmetric_difference(b)
{10, 11, 12, 16, 17, 18}
b.symmetric_difference(a)
{10, 11, 12, 16, 17, 18}
#intersection_update()
a={8,9,10,11,12}
b={11,12,13,14,15}
a.intersection_update(b)
a
{11, 12}
a
{11, 12}
b.intersection_update(b)
b
{11, 12, 13, 14, 15}
b.intersection_update(a)
b
{11, 12}
b
{11, 12}
#difference_update()
a={10,20,30,40,50}
b={30,40,50,60,70}
a.difference_update(b)
a
{20, 10}
b.difference_update(a)
b
{50, 70, 40, 60, 30}
#symetric_update()
a={3,4,5,6,7,8,9}
b={1,2,3,4,5,6}
a.symmetric_difference_update(b)
a
{1, 2, 7, 8, 9}
a
{1, 2, 7, 8, 9}
b.symmetric_difference_update(a)
b
{3, 4, 5, 6, 7, 8, 9}
#pop()
a={7,8,9,10,11,12}
a.pop()
7
a.pop(3)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    a.pop(3)
TypeError: set.pop() takes no arguments (1 given)
a
{8, 9, 10, 11, 12}
a.remove(10)
a
{8, 9, 11, 12}
a.discard(11)
a
{8, 9, 12}
a={10,20,30,40,50}
a.copy()
{50, 20, 40, 10, 30}
b=a.copy()
b
{50, 20, 40, 10, 30}
a.clear()
>>> a
set()
>>> b=set()
>>> b.add
<built-in method add of set object at 0x000001D209D7BAE0>
>>> b.add(30)
>>> b
{30}
>>> #index()
>>> a={5,6,7,8,9,10,11,12}
>>> a.index()
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    a.index()
AttributeError: 'set' object has no attribute 'index'
>>> len(a)
8
>>> a.count(10)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    a.count(10)
AttributeError: 'set' object has no attribute 'count'
>>> #isdisjoint()
>>> a={4,5,6,7,8}
>>> b={9,10,11,12,13}
>>> a.isdisjoint(b)
True
>>> a={3,4,5,6,7}
>>> b={7,8,9,10,11}
>>> a.isdisjoint(b)
False
