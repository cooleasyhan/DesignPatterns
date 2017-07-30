from cowpy import cow

def cow_style(msg):
    return cow.milk_random_cow(msg)
def default_style(msg):
    return msg

def do_print(msg, style=default_style):
    print('-' * 20)
    print(style(msg))

    print('-'*20)

def main():
    [do_print('Oh, Hello World', style) for style in [cow_style, default_style]]

if __name__ == '__main__':
    main()