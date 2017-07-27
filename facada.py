import abc
import enum

State = enum('State', 'new running sleeping restart zombie')


class Service(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def start(self):
        pass

    def __str__(self):
        return self.name

    @abc.abstractmethod
    def kill(self):
        pass


class FileService:
    def __init__(self):
        self.name = 'FileService'
        self.state = State.new

    def start(self):
        self.state = State.running

    def kill(self, restart=True):
        self.state = State.restart if restart else State.zombie

    def create_file(self, user, name, permissions):
        print("trying to create the file '{}' for user '{}' with permissions{}".format(
            name, user, permissions))


class NetwrokService:
    pass


class CpuService:
    pass


class OperatingSystem():
    def __init__(self):
        self.fs = FileService()
        self.ns = NetwrokService()
        self.cs = CpuService()

    def create_file(self, *args, **kwargs):
        self.fs.create_file(self, *args, **kwargs)

    def start(self):
        [i.start() for i in (self.fd, self.ns, self.cs)]
    
    def kill(self, restart=True):
        [i.kill(restart) for i in (self.fd, self.ns, self.cs)]
        
