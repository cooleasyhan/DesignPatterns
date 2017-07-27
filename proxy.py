class LazyProperty:
    def __init__(self, fun):
        self.fun = fun
        self.fun_name = fun.__name__

    def __get__(self, obj, cls):
        if not obj:
            