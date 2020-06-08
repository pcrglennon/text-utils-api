import itertools
import re

# TODO - make this a class!

def cross_text(text: str, axis_index: int = 0) -> str:
    if not 0 <= axis_index < len(text):
        return

    raw_text_components = split_text(text)
    text_components = format_text_components(raw_text_components)

    vertical_axis_padding = ' ' * (axis_index * 2)
    string = ''

    # vertical axis (start)
    for component in text_components[:axis_index]:
        string += f'{vertical_axis_padding}{component}\n'

    # horizontal axis
    string += ' '.join(component for component in text_components)

    # vertical axis (end)
    for component in text_components[(axis_index + 1):]:
        string += f'\n{vertical_axis_padding}{component}'

    return string

# 'Hello :smile: Hi' => ['H', 'e', 'l', 'l', 'o', ' ', ':smile:', ' ', 'H', 'i']
def split_text(text: str) -> [str]:
    text_components = re.split(r'(:[^:]+:)', text)
    text_components = list(map(
        lambda string: [string] if re.match(r':[^:]+:', string) else list(string),
        text_components
    ))
    return list(itertools.chain.from_iterable(text_components))

# upcase single characters, ignore colon-emoji strings
def format_text_components(text_components: [str]) -> [str]:
    return list(map(
        lambda string: string if re.match(r':[^:]+:', string) else string.upper(),
        text_components
    ))
