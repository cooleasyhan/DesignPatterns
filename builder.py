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