print(list(map(lambda x:x*x,[1,2,3])))



def square(x):
    return x*x
def cube(x):
    return x*x*x
funcs=[square,cube]

for r in range(5):
    value=map(lambda x:x(r),funcs)
    print(list(value))


a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]
print(list(filter(lambda x: x in a, b)))


from functools import reduce
a=[1,2,3,4,5,6]

print(reduce((lambda x,y:x*y),a))
