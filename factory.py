"""
工厂模式
实例：http://django.wikispaces.asu.edu/*NEW*+Django+Design+Patterns
"""
class HandlerClassA(object):
    def do_somthing(self):
        pass

class HandlerClassB(object):
    def do_somthing(self):
        pass

def handler_factory(para):
    if para = 'A':
        return HandlerClassA()
    elif para = 'B':
        return HandlerClassB()
    else:
        raise Exception('Unkonw para')
    
def main():
    handler = handler_factory('A')
    handler.do_somthing()

if __name__ == '__main__':
    main()