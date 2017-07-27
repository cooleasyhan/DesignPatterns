import enum
import threading
import random
TreeType = enum.Enum('TreeType', 'apple_tree cherry_tree peach_tree')

class Tree:
    pool = {}
    def __new__(cls, tree_type):
        if tree_type in cls.pool:
            return cls.pool[tree_type]
        with threading.Lock():
            if tree_type in cls.pool:
                return cls.pool[tree_type]
            cls.pool[tree_type] = super(Tree, cls).__new__(cls)
            cls.pool[tree_type].tree_type = tree_type
            return cls.pool[tree_type]

    def render(self, age, x, y):
        print('render a tree of type {} and age {} at ({}, {})'.format(self.tree_type, age, x, y))


def main():
    for i in range(100):
        tree_type = random.choice([i for i in TreeType])
        x = random.randint(1,100)
        y = random.randint(1,100)
        age = random.randint(1,18)
        t1 = Tree(tree_type)
        t1.render(age, x, y)
    print(Tree.pool)

if __name__ == '__main__':
    main()
