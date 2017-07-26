import threading
import time


def check(cls):
    print('-' * 50)
    print('check', cls)
    s1 = cls()
    s2 = cls()

    assert id(s1) == id(s2)


# Version1 不推荐这种方法，__init__执行多次
class Singletion():
    _instance = None

    def __init__(self):
        print('Singletion __init__')
        '''
        __init__ 不能有内容，每次 s = Singletion()均会调用，并初始化，造成错误的结果
        '''

    def __new__(cls, *args, **kwargs):
        if cls._instance:

            return cls._instance
        else:
            with threading.Lock():
                if not cls._instance:
                    # 此处super代表object
                    cls._instance = super(Singletion, cls).__new__(
                        cls, *args, **kwargs)
                return cls._instance


check(Singletion)


# for i in range(100):
#     def f(): return print(id(Singletion()))
#     threading.Thread(target=f).start()

# time.sleep(5)


# Version2
class SingletionMetaClass(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(
                SingletionMetaClass, cls).__call__(*args, **kwargs)
        return cls._instance[cls]


class Singletion1(metaclass=SingletionMetaClass):
    def __init__(self):
        print('Singletion1 __init__')


class Singletion2(metaclass=SingletionMetaClass):
    def __init__(self):
        print('Singletion2 __init__')


check(Singletion1)
check(Singletion2)


from functools import wraps


def singletion(cls):
    _instance = {}

    @wraps(cls)
    def warpper(*args, **kwargs):
        if cls in _instance:
            return _instance[cls]
        else:
            with threading.Lock():
                if cls in _instance:
                    return _instance[cls]
                else:
                    _instance[cls] = cls(*args, **kwargs)
                    return _instance[cls]
    return warpper


@singletion
class ClassA():
    def __init__(self):
        '''
        init 方法只执行一次
        '''
        print('@singletion __init__')


check(ClassA)
