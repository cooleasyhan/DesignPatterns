"""
元类就是用来定义类的类
"""

# type 是所有python对象默认的元类


class A:
    pass


a = A()
print(a.__class__)  # <class '__main__.A'>
print(a.__class__.__class__)  # <class 'type'>

print('-'*50)

class Metaclass(type):

    def __prepare__(metacls, name, bases=None):
        """
        返回一个dict
        """
        return dict()

    def __new__(cls, name, bases, dct):
        print('Metaclass Enter New')
        """
        cls: 指向的是 Metaclass 本身
        name: 类对象
        bases: 类的父类
        dct: 类的属性
        """
        dct['attr_add_by_Metaclass__new__'] = 'attr_add_by_Metaclass__new__'
        return super(Metaclass, cls).__new__(cls, name, bases, dct)

# metaclass 可以直接执行生成ClassA
ClassA = Metaclass(
    'ClassA', (), {'attr_add_by_Metaclass': 'attr_add_by_Metaclass'})

print(ClassA) #<class '__main__.ClassA'>

a = ClassA()
print(a.attr_add_by_Metaclass__new__)
print(a.attr_add_by_Metaclass)

print('-'*50)

class MyObject(object,metaclass=Metaclass):
    pass

b = MyObject()
print(b.attr_add_by_Metaclass__new__)

