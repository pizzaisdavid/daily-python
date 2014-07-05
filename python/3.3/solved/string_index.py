def string_index(string, indices):
    indices = setup(indices)
    words = get_words(string)
    message = select_words(indices, words)
    print(' '.join(message))

def setup(data):
    datas = [number for number in data.split()]
    indices = []
    for data in datas:
        indices.append(int(data))
    return indices

def get_words(string):
    alphabet = 'acbdefghijklmnopqrstuvwxyz'
    number = '1234567890'
    word = ''
    EMPTY = ''
    message = []
    for character in string:
        if character.lower() in alphabet or character in number:
            word += character
        elif word != EMPTY:
            message.append(word)
            word = ''
    return message

def select_words(indices, words):
    message = []
    for index in indices:
        if index > 0:
            try:
                message.append(words[index - 1])
            except:
                pass
    return message

string_index('...You...!!!@!3124131212 Hello have this is a --- string Solved !!...? to test @\n\n\n#!#@#@%$**#$@ Congratz this!!!!!!!!!!!!!!!!one ---Problem\n\n',
             '12 -1 1 -100 4 1000 9 -1000 16 13 17 15')
