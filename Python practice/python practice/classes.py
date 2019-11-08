class Snake:
    name='python'
    def change_name(self,new_name):
        self.name=new_name

snake=Snake()
snake.change_name('anaconda')
print(snake.name)



class Snake:
    def __init__(self,name):
        self.name=name
    def change_name(self,new_name):
        self.name=new_name



snake1=Snake('python')
print(snake1.name)
snake2=Snake('anaconda')
print(snake2.name)



try:
    print('in try block')
    print(1/0)
except:
    print('in the except block')
finally:
    print('in finally block')


'''try:
    inp=int(input())
    if inp<0:
        raise ValueError('please give positive no')
    else:
        print('input is %s'%inp)
except ValueError as e:
    print(e)
'''

def vowels():
    yield ['a','e','i','o']

print(next(vowels()))


for each in vowels():
    print(each)