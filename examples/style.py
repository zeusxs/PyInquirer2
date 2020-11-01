from prompt_toolkit.styles import Style

custom_style_1 = Style.from_dict({
    "separator": '#cc5454',
    "questionmark": '#673ab7 bold',
    "focus": '#cc5454',  # default
    "checked": '#cc5454',
    "pointer": '#673ab7 bold',
    "instruction": '',  # default
    "answer": '#f44336 bold',
    "question": '',
})

custom_style_2 = Style.from_dict({
    "separator": '#6C6C6C',
    "questionmark": '#FF9D00 bold',
    "focus": '#5F819D',
    "checked": '#FF9D00',
    "pointer": '#FF9D00 bold',
    "instruction": '',  # default
    "answer": '#5F819D bold',
    "question": '',
})

custom_style_3 = Style.from_dict({
    "questionmark": '#E91E63 bold',
    "focus": '#673AB7 bold',
    "checked": '#5F819D',
    "instruction": '',  # default
    "answer": '#2196f3 bold',
    "question": '',
})
