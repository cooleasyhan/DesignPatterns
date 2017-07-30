class Event:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

class Handler:
    def __init__(self, parent=None):
        self.parent = parent
    
    def handle(self, event):
        handler = f'handle_{event}'
        if hasattr(self, handler):
            getattr(self, handler)(event)
        elif self.parent:
            self.parent.handle(event)
        else:
            self.handle_default(event)


class HtmlHandler(Handler):
    def handle_render(self, event=None):
        print(f'HtmlHandler Handle {event}')

    def handle_default(self, event):
        print(f'Handle Default {event}')

class ButtonHandler(Handler):
    def handle_new_button(self, event):
        print(f'ButtonHandler handle {event}')

class ClickHandler(Handler):
    def handle_click(self, event):
        print(f'Click Handler {event}')


if __name__ == '__main__':
    html_handler = HtmlHandler()
    button_handler = ButtonHandler(html_handler)
    click_handler = ClickHandler(button_handler)

    for event in ('render', 'new_button', 'click', 'close'):
        evt = Event(event)
        html_handler.handle(evt)
        button_handler.handle(evt)
        click_handler.handle(evt)