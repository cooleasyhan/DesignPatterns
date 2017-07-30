
# observer.py

#%%

import abc

class Publisher:
    def __init__(self):
        self.observers = []

    def add(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
        else:
            raise Exception('Error Add')

    def remove(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            raise Exception('Error Remove')

    def notify(self):
        [o.notify(self) for o in self.observers]


class Observer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def notify(self, publisher):
        pass


class DataPublisher(Publisher):
    def __init__(self, name, data=None):
        super(DataPublisher, self).__init__()

        self.name = name
        self._data = data

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_value):
        self._data = new_value
        self.notify()


class HtmlReader(Observer):
    def notify(self, publisher):
        print(f'<html><body><h1>Get Data {publisher.data} from publisher {publisher.name}<h1></body></html>')

class TextReader(Observer):
    def notify(self, publisher):
        print(f'Get Data {publisher.data} from publisher {publisher.name}')


d = DataPublisher(name='Test')
html_reader= HtmlReader()
text_reader = TextReader()

d.add(html_reader)
d.add(text_reader)

d.data = 'Oh No'

d.data = 'My God'
