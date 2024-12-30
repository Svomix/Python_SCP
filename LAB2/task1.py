import string


def read_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return ''.join((x.lower() for x in file.read() if x not in string.punctuation)).split()
