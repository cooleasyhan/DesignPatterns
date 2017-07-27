class Computer:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f'the {self.name} computer'

    def execute(self):
        return 'execute a program'

class Human:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
       return f'the {self.name} human' 

    def speak(self):
        return 'says hello'

class Adapter:
    def __init__(self, obj, adapt_methods):
        self.obj = obj
        self.__dict__.update(adapt_methods)

    def __str__(self):
        return str(self.obj)

def client(obj):
    print(obj, obj.execute())

client(Computer('ThinkPad T400'))
h = Human('YH')
client(Adapter(h, {'execute':h.speak}))