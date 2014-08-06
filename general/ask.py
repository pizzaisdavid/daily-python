def ask(options, prompt):
    answer = input(prompt).lower()
    while answer not in options:
        answer = input('Please enter in one of the following: {0}'.format(options))
    return answer
    
