import copy 
class Prototype:
    def __init__(self):
        self.objects = {}

    def register(self, identifier, obj):
        self.objects[identifier] = obj
    
    def unregister(self, identifier):
        del self.objects[identifier]
    
    def clone(self, identifier, **kwargs):
        obj = copy.deepcopy(self.objects[identifier])
        obj.__dict__.update(kwargs)
        return obj

def main():
    obj = Prototype()
    p = Prototype()
    p.register('id', obj)
    new_p = p.clone('id',a='a')

    print(id(p), id(new_p))

if __name__ == '__main__':
    main()