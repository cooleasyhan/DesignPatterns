import abc


class Command(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def execute(self):
        pass

    @abc.abstractmethod
    def undo(self):
        pass


class RenameFile:
    def __init__(self, src_file, dest_file):
        self.src_file = src_file
        self.dest_file = dest_file

    def execute(self):
        print(f'rename file {self.src_file} to {self.dest_file}')

    def undo(self):
        print(f'rename file {self.dest_file} to {self.src_file}')


class CreateFile:
    def __init__(self, path, text='HelloWorld\n'):
        self.path = path
        self.text = text

    def execute(self):
        print(f'Create File {self.path}, text: {self.text}')

    def undo(self):
        print(f'delete file {self.path}')


class DeleteFile:
    is_undo = False

    def __init__(self, path):
        self.path = path

    def execute(self):
        print(f'delete file {self.path}')

    def undo(self):
        raise Exception('Can not undo')

def main():
    cmds = (RenameFile('/tmp/a','/tmp/b'), CreateFile('/tmp/c'))
    for c in cmds: 
        c.execute()

    for c in reversed(cmds):
        c.undo() 

if __name__ == '__main__':
    main()