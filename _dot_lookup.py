"""
1. __getattribute__ 会有最高权限， 如果存在 __getattribute__ 会最先调用， 如果没有，则会调用基类的__getattribute__， 
一般会是object.__getattribute__, object.__getattribute__ 定义了寻找定义的常规路径

2. 查找 obj.__dict__, 如果存在则返回，除非存在  "data descriptors"， 典型是@property， descriptor 里的__get__ __set__方法会被调用

3. 查找 super(obj).__dict__,遵循 mro， data descriptors 仍然生效

4. 找到属性，但是存在 A non-data descriptor ， 存在 __get__, 但是不存在 __set__, 这个non-data descriptor 会变成object的一个bound method， (this is how Python can pass the object as the first argument automatically). 
__get__ 方法会被调用

5. 如果都没有找到， 则会调用__getattr__


It's a bit complicated. Here's the sequence of checks Python does if you request an attribute of an object.

First, Python will check if the object's class has a __getattribute__ method. If it doesn't have one defined, 
it will inherit object.__getattribute__ which implements the other ways of finding the attribute's values.

The next check is in the object's class's __dict__. However, even if a value is found there, 
it may not be the result of the attribute lookup! Only "data descriptors" will take precedence if found here.
 The most common data descriptor is a property object, which is a wrapper around a function that will be called each time an attribute is accessed.
  You can create a property with a decorator:


class foo(object):
    @property
    def myAttr(self):
        return 2
In this class, myAttr is a data descriptor. That simply means that it implements the descriptor protocol by having both __get__ and __set__ methods. A property is a data descriptor.

If the class doesn't have anything in its __dict__ with the requested name, object.__getattribute__ searches through its base classes (following the MRO) to see if one is inherited.
 An inherited data descriptor works just like one in the object's class.

If a data descriptor was found, it's __get__ method is called and the return value becomes the value of the attribute lookup. 
If an object that is not a data descriptor was found, it is held on to for a moment, but not returned just yet.

Next, the object's own __dict__ is checked for the attribute. This is where most normal member variables are found.

If the object's __dict__ didn't have anything, but the earlier search through the class (or base classes) found something other than a data descriptor,
 it takes next precedence. An ordinary class variable will be simply returned, but "non-data descriptors" will get a little more processing.

A non-data descriptor is an object with a __get__ method, but no __set__ method. The most common kinds of non-data descriptors are functions, 
which become bound methods when accessed as a non-data descriptor from an object (this is how Python can pass the object as the first argument automatically). 
The descriptor's __get__ method will be called and it's return value will be the result of the attribute lookup.

Finally, if none of the previous checks succeeded, __getattr__ will be called, if it exists.

Here are some classes that use steadily increasing priority attribute access mechanisms to override the behavior of their parent class:


class O1(object):
    def __getattr__(self, name):
        return "__getattr__ has the lowest priority to find {}".format(name)

class O2(O1):
    var = "Class variables and non-data descriptors are low priority"
    def method(self): # functions are non-data descriptors
        return self.var

class O3(O2):
    def __init__(self):
        self.var = "instance variables have medium priority"
        self.method = lambda: self.var # doesn't recieve self as arg

class O4(O3):
    @property # this decorator makes this instancevar into a data descriptor
    def var(self):
        return "Data descriptors (such as properties) are high priority"

    @var.setter # I'll let O3's constructor set a value in __dict__
    def var(self, value):
        self.__dict__["var"]  = value # but I know it will be ignored

class O5(O4):
    def __getattribute__(self, name):
        if name in ("magic", "method", "__dict__"): # for a few names
            return super(O5, self).__getattribute__(name) # use normal access

        return "__getattribute__ has the highest priority for {}".format(name)
And, a demonstration of the classes in action:

O1 (__getattr__):


>>> o1 = O1()
>>> o1.var
'__getattr__ has the lowest priority to find var'
O2 (class variables and non-data descriptors):


>>> o2 = O2()
>>> o2.var
Class variables and non-data descriptors are low priority'
>>> o2.method
<bound method O2.method of <__main__.O2 object at 0x000000000338CD30>>
>>> o2.method()
'Class variables and non-data descriptors are low priority'
O3 (instance variables, including a locally overridden method):


>>> o3 = O3()
>>> o3.method
<function O3.__init__.<locals>.<lambda> at 0x00000000034AAEA0>
>>> o3.method()
'instance variables have medium priority'
>>> o3.var
'instance variables have medium priority'
O4 (data descriptors, using the property decorator):


>>> o4 = O4()
>>> o4.method()
'Data descriptors (such as properties) are high priority'
>>> o4.var
'Data descriptors (such as properties) are high priority'
>>> o4.__dict__["var"]
'instance variables have medium priority'
O5 (__getattribute__):


>>> o5 = O5()
>>> o5.method
<function O3.__init__.<locals>.<lambda> at 0x0000000003428EA0>
>>> o5.method()
'__getattribute__ has the highest priority for var'
>>> o5.__dict__["var"]
'instance variables have medium priority'
>>> o5.magic
'__getattr__ has the lowest priority to find magic'
"""




class O1(object):
    def __getattr__(self, name):
        return "__getattr__ has the lowest priority to find {}".format(name)

class O2(O1):
    var = "Class variables and non-data descriptors are low priority"
    def method(self): # functions are non-data descriptors
        return self.var

class O3(O2):
    def __init__(self):
        self.var = "instance variables have medium priority"
        self.method = lambda: self.var # doesn't recieve self as arg

class O4(O3):
    @property # this decorator makes this instancevar into a data descriptor
    def var(self):
        return "Data descriptors (such as properties) are high priority"

    @var.setter # I'll let O3's constructor set a value in __dict__
    def var(self, value):
        print('Data descriptors Setter')
        self.__dict__["var"]  = value # but I know it will be ignored

class O5(O4):
    def __getattribute__(self, name):
        if name in ("magic", "method", "__dict__"): # for a few names
            return super(O5, self).__getattribute__(name) # use normal access

        return "__getattribute__ has the highest priority for {}".format(name)


print('O1', '-'*50)
o1 = O1()
print(o1.var)
print('O2', '-'*50)
o2 = O2()
print(o2.var)
print(o2.method)
print(o2.method())

print('O3', '-'*50)

o3 = O3()
print(o3.method)
print(o3.method())
print(o3.var)

print('O4', '-'*50)
o4 = O4()
print(o4.method())
print(o4.var)
print(o4.__dict__["var"])

print('O5', '-'*50)

o5 = O5()
print(o5.method)
print(o5.method())
print(o5.__dict__["var"])
print(o5.magic)
