a = 5
print("Type of a: ", type(a))
  
b = 5.0
print("\nType of b: ", type(b))
  
c = 2 + 4j
print("\nType of c: ", type(c))

String1 = 'Hello World'
print(String1) 
print(type(String1))
    
String1 = "Hello's World"
print(String1) 
print(type(String1))
 
String1 = '4'
String2 = '5'
print(int(String1)*float(String2)) 
print(type(int(String1)))
  
String1 = '''Hello "world"'''
print(String1) 
print(type(String1))
  
String1 = '''Hello 
            world'''
print(String1) 
print(type(String1))

String1 = 'Hello World'
print(String1[0])
print(String1[1])
print(String1[-1])
 
List = [['Apple', 'Banana'], ['Carrot']] 
print(List) 
print(List[0][-1]) 

Tuple1 = (0, 5, 1, 2, 3) 
Tuple2 = ('hello', 'world') 
Tuple3 = (Tuple1, Tuple2) 
print(Tuple1)
print(Tuple2)
print(Tuple3)
print(Tuple3[0][1])

print(type(True))
print(type(False))

set1 = set() 
set2 = set(['abc','def',(5,4,6)]) 
print(set1) 
for i in set2: 
    print(i, end ="|")
print("\nSet contents:"+str(set2))
print(set2.pop())

diary: dict = {"month":"may", "city":"new york"}
print(diary)
print(diary.get('city'))
print(diary.keys())
print(diary.values())
diary = dict([(1, 'may'), (2, 'new york')])
print(diary.get(2))
print(diary.keys())
print(diary.values())