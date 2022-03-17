morse_code = {
    'A': '•-',
    'B': '-•••',
    'C': '-•-•',
    'D': '-••',
    'E': '•',
    'F': '••-•',
    'G': '--•',
    'H': '••••',
    'I': '••',
    'J': '•---',
    'K': '-•-',
    'L': '•-••',
    'M': '--',
    'N': '-•',
    'O': '---',
    'P': '•--•',
    'Q': '--•-',
    'R': '•-•',
    'S': '•••',
    'T': '-',
    'U': '••-',
    'V': '•••-',
    'W': '•••-',
    'X': '-••-',
    'Y': '-•--',
    'Z': '--••',
    '1': '•----',
    '2': '••---',
    '3': '•••--',
    '4': '••••-',
    '5': '•••••',
    '6': '-••••',
    '7': '--•••',
    '8': '---••',
    '9': '----•',
    '0': '-----',
}

text = input("Type text to code: ")


def split(word):
    return [char.upper() for char in word]


text_to_code = split(text)
code = [morse_code[char] for char in text_to_code]
result = ' '.join(code)
print(result)