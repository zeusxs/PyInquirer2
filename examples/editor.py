# -*- coding: utf-8 -*-
"""
* Editor prompt example
"""
from pprint import pprint
from inquirer2 import prompt, print_json

from style import custom_style_2

questions = [
    {
        'type': 'editor',
        'name': 'bio',
        'message': 'Please write a short bio of at least 3 lines.',
        'default': 'Hello World',
        'validate': lambda text: len(text.split('\n')) >= 1 or 'Must be at least 3 lines.',
        'eargs': {
            'editor':'nano',
            'ext':'.py'
        }
    }
]

answers = prompt.prompt(questions, style=custom_style_2)
pprint(answers)
