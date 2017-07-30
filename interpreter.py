"""
command token receiver token arguments
"""

from pyparsing import Word, Group, Suppress, Optional, OneOrMore, alphanums

def init_parse():
    word = Word(alphanums)
    command = Group(OneOrMore(word))
    token = Suppress('->')
    device = Group(OneOrMore(word))
    argument = Group(OneOrMore(word))

    event = command + token + device + Optional(token + argument)

    return event

class Door:
    def open(self):
        print('Open the Door')

    def close(self):
        print('Close the door')

door = Door()
actions = {'door.open':door.open, 'door.close':door.close}



def main():
    event = init_parse()
    cmd_str = 'open -> door'
    cmd, device = event.parseString(cmd_str)
    action_name = '.'.join([' '.join(device), ' '.join(cmd)])
    action = actions[action_name]
    action()


if __name__ == '__main__':
    main()


