"""
因为抽象工厂模式是工厂方法模式的一种泛化，所以它能提供相同的好处:让对象的创建更容易追踪;
将对象创建与使用解耦;提供优化内存占用和应用性能的潜力。
这样会产生一个问题:我们怎么知道何时该使用工厂方法，何时又该使用抽象工厂?
答案是， 通常一开始时使用工厂方法，因为它更简单。如果后来发现应用需要许多工厂方法，
那么将创建 一系列对象的过程合并在一起更合理，从而最终引入抽象工厂。
抽象工厂有一个优点，在使用工厂方法时从用户视角通常是看不到的，
那就是抽象工厂能够 通过改变激活的工厂方法动态地(运行时)改变应用行为。
一个经典例子是能够让用户在使用应 用时改变应用的观感(比如，Apple风格和Windows风格等)，
而不需要终止应用然后重新启动(请 参考[GOF95，第99页])。

应用实例：https://pypi.python.org/pypi/django_factory/0.7
"""

import abc
import asyncio
from asyncio import get_event_loop


class Character(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def interact_with(self, obstacle):
        pass


class Obstacle(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def action(self):
        pass

class World(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def make_character(self):
        pass

    @abc.abstractmethod
    def make_obstacle(self):
        pass


class Frog(Character):
    def __init__(self, name):
        self.name = name

    def interact_with(self, obstacle):
        print('{} the Frog encounters {} and {}!'.format(
            self, obstacle, obstacle.action()))

class Bug(Obstacle):
    def __str__(self):
        return ' a bug'
    def action(self):
        return 'eats it'

class Wizard(Character):
    def __init__(self, name):
        self.name = name
    
    def interact_with(self, obstacle):
        print('{} the Wizard battles against {} and {}!'.format(self,obstacle, obstacle.action()))

class Ork(Obstacle):
    def __str__(self):
        return 'a ork'
    def action(self):
        return 'kills it'

class FrogWorld(World):
    def __init__(self, name):
        print(self)
        self.player_name = name
    def __str__(self):
        return '\n\n\t------ Frog World-------'
    def make_character(self):
        return Frog(self.player_name)
    def make_obstacle(self):
        return Bug()


class WizardWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name
    def __str__(self):
        return '\n\n\t------ Wizard World -------'
    def make_character(self):
        return Wizard(self.player_name)
    def make_obstacle(self):
        return Ork()

class GameEnviroment:
    def __init__(self, factory):
        self.character = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.character.interact_with(self.obstacle)



def main():
    name = 'HelloWorld'
    age = 11
    game = WizardWorld if age >= 18 else FrogWorld
    g = GameEnviroment(game(name))
    g.play()


if __name__ == '__main__':
    main()
