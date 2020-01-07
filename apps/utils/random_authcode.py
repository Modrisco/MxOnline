import string
from random import choice


def generate_random(random_length, type):
    '''
    generate random authentication code string according to length and type
    :param random_length: authentication code string length
    :param type: authentication code string type (0: digits, 1: digits + char, 2: digits + char + special characters)
    :return: generated authentication code string
    '''
    if type == 0:
        random_seed = string.digits
    elif type == 1:
        random_seed = string.digits + string.ascii_letters
    elif type == 2:
        random_seed = string.digits + string.ascii_letters + string.punctuation
    random_str = []
    while len(random_str) < random_length:
        random_str.append(choice(random_seed))
    return ''.join(random_str)
