Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=[9,1,5,2,8,4,6,3,7,0]
>>> #[7,6,4,3,0,9,8,5,2,1]
>>> type(a)
<class 'list'>
>>> a1=a[0:5]
>>> a1
[9, 1, 5, 2, 8]
>>> a2=a[5:10]
>>> a2
[4, 6, 3, 7, 0]
>>> a1.sort()
>>> a1
[1, 2, 5, 8, 9]
>>> a2.sort()
>>> a2
[0, 3, 4, 6, 7]
>>> a1.reverse()
>>> a1
[9, 8, 5, 2, 1]
>>> a2.reverse()
>>> a2
[7, 6, 4, 3, 0]
>>> c=a2+a1
>>> c
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1]
>>> #dict{}
>>> a={"name":"gopi":2026,"month":10}
SyntaxError: invalid syntax
>>> a={"name":"gopi","year":2026,"month":10}
>>> print(a)
{'name': 'gopi', 'year': 2026, 'month': 10}
type(a)
<class 'dict'>
a={"year":2026,"month":"oct","date":31}
a.keys()
dict_keys(['year', 'month', 'date'])
a.values()
dict_values([2026, 'oct', 31])
a.items()
dict_items([('year', 2026), ('month', 'oct'), ('date', 31)])
b={1:2,3:4}
type(b)
<class 'dict'>
a.keys()
dict_keys(['year', 'month', 'date'])
a={"course":"python","code":"gnan","data":"coding"}
a{"course"}
SyntaxError: invalid syntax
a["course"]
'python'
a
{'course': 'python', 'code': 'gnan', 'data': 'coding'}
a["python"]
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    a["python"]
KeyError: 'python'
a.get("code")
'gnan'
a
{'course': 'python', 'code': 'gnan', 'data': 'coding'}
a.get("data")
'coding'
a
{'course': 'python', 'code': 'gnan', 'data': 'coding'}
a={"year":2026,"month":11}
a.update({"time":10})
a
{'year': 2026, 'month': 11, 'time': 10}
a.update({"hour":1,{"min":10})
         
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
a.update({"hour":1},{"min":10})
         
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    a.update({"hour":1},{"min":10})
TypeError: update expected at most 1 argument, got 2
a.update({"hour":1,"min":10})
         
a.update({"hour":1,"min":10})
         
a
         
{'year': 2026, 'month': 11, 'time': 10, 'hour': 1, 'min': 10}
a={"colour":"black","food":"biryani","desert":"cake"}
         
a.setdefault("place","vja")
         
'vja'
a
         
{'colour': 'black', 'food': 'biryani', 'desert': 'cake', 'place': 'vja'}
a.pop()
         
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop("colour")
         
'black'
a
         
{'food': 'biryani', 'desert': 'cake', 'place': 'vja'}
a.popitem()
         
('place', 'vja')
a
         
{'food': 'biryani', 'desert': 'cake'}
a={"hour":10,"min":11,"sec":5}
         
a.copy()
         
{'hour': 10, 'min': 11, 'sec': 5}
a.clear()
         
a
         
{}


a={"name":"gopi","city":"gnt","name":"gopi"}
         
print(a)
         
{'name': 'gopi', 'city': 'gnt'}
a={"name":"gopi","city":"gnt","name":"krishna"}
         
print(a)
         
{'name': 'krishna', 'city': 'gnt'}
a={"name1":"gopi","city":"gnt","name2":"gopi"}
         
print(a)
         
{'name1': 'gopi', 'city': 'gnt', 'name2': 'gopi'}
a={"idnos":[10,20,30],"names":["pooja","preethi","priya"],"marks":[60,70,80]}
         
print(a)
         
{'idnos': [10, 20, 30], 'names': ['pooja', 'preethi', 'priya'], 'marks': [60, 70, 80]}
type(a)
         
<class 'dict'>
a.keys()
         
dict_keys(['idnos', 'names', 'marks'])
a.values()
         
dict_values([[10, 20, 30], ['pooja', 'preethi', 'priya'], [60, 70, 80]])
a.items()
         
dict_items([('idnos', [10, 20, 30]), ('names', ['pooja', 'preethi', 'priya']), ('marks', [60, 70, 80])])

