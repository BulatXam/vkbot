import json

class Vk_Keyboard:
    def __init__(self, one_time=False, inline=False):
        self.one_time = one_time
        self.inline = inline
        self.buttons = []
        self.lines = [self.buttons]

        self.keyboard = {
            'one_time':self.one_time,
            'inline':self.inline,
            'buttons':self.lines
        }

        # self.get_keyboard()

    def get_keyboard(self):
        return json.dumps(self.keyboard)

    def add_button(self, btn_type, label, color='positive', payload=''):
        button_json = {
            'action':{
                'type':btn_type,
                'payload':payload,
                'label':label
            },
            'color':color
        }
        self.buttons.append(button_json)