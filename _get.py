"""
1. __getattribute__最先执行， 如果显示Raise AttributeError会接着执行__getattr__, 显示调用__getattr__或者__dict__均会抛出RecurisonError
2. 
"""

class B:
    b = 'b'
    # def __getattr__(self, attr):
    #     print('B: __getattr__')
    #     return 1


class C(B):
    pass

class A(B):
    def __init__(self, a):
        self.a = a

    def __getattribute__(self, attr):
        print('__getattribute__')
        return super(A, self).__getattr__(attr)
        return self.attr
        # raise AttributeError()
        # return self.__dict__[attr]
        # return 'get from __getattribute__' 
    
    def aa(self):
        return 'jjj'

    def __getattr__(self, attr):
        print('A:__getattr__')
        # raise AttributeError()
        return 'get from __getattr__'

    def __get__(self, obj, cls):
        print('__get__')


b = B()
print(dir(b))
a = A(1)

print(a.__mro__)
print(a.a)

class Test(B):
    def __init__(self,name):
        self.name = name
    def __getattribute__(self, value):
        if value == 'address':
            return 'China'
        return object.__getattribute__(self, value)
        # raise AttributeError

t = Test(1)
print(t.b)

print(dir(object))