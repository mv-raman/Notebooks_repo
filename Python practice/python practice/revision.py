print(isinstance(2.0,int))
print('hi')
result=3/2
print(result)
print(isinstance(result,float))
print("abcde".index('c'))
combined_string=',""'.join(['1','2','3'])
print(combined_string)
print('1,2,3'.split(','))
print('abcd %s and %s' %('asdf','jkldsf'))
print('PYTHON IN  {sdfklj} & {sdf}'.format(sdfklj='pycharm',sdf='jupyter'))
langs = ["haskell", "clojure", "apl"]
langs.extend(["scala", "F#"])
print(langs)
alphabets = {1:"a"}
print(alphabets[1])

print(alphabets.get(2,'default'))

person1_information = {'city': 'San Francisco', 'name': 'Sam', "food": "shrimps"}

print(person1_information.pop('city'))
print(person1_information)
seta=set([1,2,3,4,])
setb=set([2,3,4,5,1])
print('-----')
print(setb.difference(seta))
print(seta.issubset(setb))


def summation(nums):
    print(sum(nums))


summation([1,2,3,4])

def myfun(*args):
    for each in args:
        print(each)

myfun(1,2,3)

def myfun(**kwargs):
    for key,value in kwargs.items():
        print(key,value)


myfun(name='venkat',company='fico')


print("------------------")

#passing function as argument to method


from functools import reduce

def sum(*args):
   return reduce(lambda x,y:x+y,args)


def printer(f,*args):
    print(f(*args))


printer(sum,1,2,3,23,5,32)


#closure


def addwith5():
    five=5
    def add(arg):
        return arg+five
    return add

closure=addwith5()
print(closure(2))



print('-***************-')

#actual use of decarator
def function():
    print('inside function')

def hellodecorator(func):
    def inner():
        print('this is before')
        func()
        print('this is after')
    return inner
funtobeused=hellodecorator(function)
funtobeused()

print('----------________________________----------------')

#one more way decorator(decorator can be used when you want to modify function but dont want to touch it by use of decorator we can call same function but with new modified functionality
import time

#writing decorator to calculate time
def timecalcdec(func):
    def inner(*args,**kwargs):
        print('before execution')
        begin= time.time()
        returned_value=func(*args,**kwargs)
        end=time.time()
        print('time to execute :',end-begin)
        return returned_value+1
    return inner

@timecalcdec
def sum_2_num(a,b):
    time.sleep(2)
    print('inside function')
    return a+b



print(sum_2_num(10,20))