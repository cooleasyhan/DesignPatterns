"""
应用实例：
django-query-builder [http://django-query-builder.readthedocs.io/en/latest/usage_examples.html]

想要创建一个复杂对象(对象由多个部分构成，且对象的创建要经过多个不同的步骤， 这些步骤也许还需遵从特定的顺序)
要求一个对象能有不同的表现，并希望将对象的构造与表现解耦 
想要在某个时间点创建对象，但在稍后的时间点再访问

"""

import abc


class Director(): 
    def __init__(self, builder):
        self._builder = builder
        self._builder.build_part_a()
        self._builder.build_part_b()
        self._builder.build_part_c()
    
    

class Product():
    pass


class Builder(metaclass=abc.ABCMeta):
    def __init__(self):
        self.product = Product()

    @abc.abstractmethod
    def build_part_a(self):
        pass

    @abc.abstractmethod
    def build_part_b(self):
        pass

    @abc.abstractmethod
    def build_part_c(self):
        pass

class ConcreteBuilder(Builder):
    def build_part_a(self):
        self.product.a = 'a'

    def build_part_b(self):
        self.product.b = 'b'

    def build_part_c(self):
        self.product.c  = 'c'

if __name__ == '__main__':
    builder = ConcreteBuilder()
    o = Director(builder)
    print(dir(builder.product))