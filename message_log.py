import textwrap
import tcod

import color

class Message:
    def __init__(self, text, fg):
        self.plain_text = text
        self.fg = fg
        self.count = 1

    @property
    def full_text(self):
        """The full text of this message, including the count"""
        if self.count > 1:
            return f"{self.plain_text} (x{self.count})"
        return self.plain_text

class MessageLog:
    def __init__(self):
        self.messages = []

    def add_message(self, text, fg=color.white, stack=True):
        """Add message to log"""
        if stack and self.messages and text == self.messages[-1].plain_text:
            self.messages[-1].count += 1
        else:
            self.messages.append(Message(text, fg))

    def render(self, console, x, y, width, height):
        """Render the log in the given area"""
        self.render_messages(console, x, y,width, height, self.messages)

    @staticmethod
    def render_messages(console, x, y, width, height, messages):
        """Render the messages provided"""
        y_offset = height - 1
        for msg in reversed(messages):
            for line in reversed(textwrap.wrap(msg.full_text, width)):
                console.print(x=x, y=y+y_offset, string=line, fg=msg.fg)
                y_offset -= 1
                if y_offset < 0:
                    return
                
            
