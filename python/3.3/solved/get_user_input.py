def get_information():
    user = {}
    prompts = {'name': 'What\'s your name?',
               'age': 'How old are you?',
               'username': 'What\'s your reddit username?'}
    for prompt in prompts:
        user[prompt] = input('{0} :'.format(prompts[prompt]))
    print('Your name is {0}, you are {1} years old, and your username is {2}'.format(user['name'],
                                                                                     user['age'],
                                                                                     user['username']))

get_information()
