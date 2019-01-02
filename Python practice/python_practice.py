print("hi")
x=1
if x==1:
    print("value of x is 1")
myint=7
print(myint)
myfloat=float(8)
print(myfloat)
one=1
two=2
three=one+two
print("three is",three)

mylist=[]
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist)
for x in mylist:
    print(x)
squared=3**2
print(squared)
cubed=4**3
print(cubed)
even_no=[2,4,6]
odd_no=[1,3,5]
joined_list=even_no+odd_no
print(joined_list)
print([1,2,3]*5)
name="venkat"
age =24
print("hello %s age %d"%(name,age))
print("hello "+name)
mylist=[1,2,3]
print(mylist)
print("%s"%mylist)
astring="helloworld"
print(astring.index('o'))
print(len(astring))
print(astring.count("l"))
print(astring[0:4])
astring = "Hello world!"
print(astring)
print(astring[3:7])
print(astring[1:10:2])
print(astring[::-1])
afewwords = astring.split(" ")
print(afewwords)
print("last five words are :"+astring[-5:])

name='venkat'
if name in ["venkat","raman"]:
    print("your name is "+name)
primes=[2,3,5,7]
for prime in primes:
    print(prime)
for x in range(1,5):
    print(x)
count=0
while count<5:
    print(count)
    count+=1
else:
    print("last value reached")

class Myclass:
    variable='blah'

    def functions(self):
        print("this method is inside class")

object=Myclass()
print(object.variable)
print(object.functions())

#dictionaries
phonebook={}
phonebook["venkat"]=9328498
phonebook["divya"]=89923
phonebook["jill"]=8239832
print(phonebook)
#or
phonebook={
    "diyva":2390,
    "venkat":230932,
    "isadfoi":239
}
print(phonebook)
print(phonebook.keys(),phonebook.values())
#another method
for keys,values in phonebook.items():
    print(keys,values)
#del phonebook["isadfoi"]
phonebook.pop("isadfoi")
print(phonebook.items())
sentence="venkat raman is a changed man now"
words=sentence.split()
print(words)
wordsnew=[]
for word in words:
    wordsnew.append(word)
print(wordsnew)

#get only +ve num in new list List comprehnsion
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]

newnum=[float(x) for x in numbers if x >0]
print(newnum)


def foo(first,second,*args):
    print(first)
    print(second)
    print(list(args))

foo(1,2,4,23,32)

def bar(a,b,c,**kwargs):
    print(kwargs.get("name"))

bar(1,2,3,name="venkat")

print(set("my name is venkat and venkat is my name".split()))
a=set(["venkat","ganesh","divya"])
b=set(["venkat","ganesh","ram"])
print(a)
print(a.intersection(b))
print(a.symmetric_difference(b))
print(a.difference(b))
print(a.union(b))


import json
json_string=json.dumps({1:"A",2:"B",3:"C"})
print(json_string)
json_loads=json.loads(json_string)
print(json_loads["2"])

#help(any)
#python
print("hi")
hw12 = '%s %s %d' % ("hello", "world", 12)  # sprintf style string formatting
print(hw12)
#string
s="hello"
print(s.capitalize())
print(s.upper())
print(s.rjust(7))
print(s.center(7))
print(s.replace('l','(ell)'))
print('wo   rld   '.strip())
#slicing
nums=list(range(5))
print(nums)
#enumerate
animals=['cat','dogs','fish']
for idx,animal in enumerate(animals):
    print(idx+1,animal)
#loops
d={'person':2,'cat':4,'spider':8}
for key in d:
    value=d[key]
    print(key,value)
for key,value in d.items():
    print(key,value)
#tuple cant add or remove elements whereas list can
d={(x,x+1):x for x in range(10)}
t=(5,6)
print(d[t])
print(d)
