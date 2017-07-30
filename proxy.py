class LazyProperty:
    def __init__(self, fun):
        self.fun = fun
        self.fun_name = fun.__name__

    def __get__(self, obj, cls):
        print('__get__', obj, cls)
        if not obj:
           return None
        value = self.fun(obj)
        setattr(obj, self.fun_name, value)
        return value


class Test:
    def __init__(self):
        self.a = 'a'

    @LazyProperty
    def b(self):
        print('cal b')
        import time
        time.sleep(1)
        return 'bbbbbbbb'

t = Test()

print(t.b)
print(t.b)