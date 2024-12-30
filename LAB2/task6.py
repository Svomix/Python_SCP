def save_data(filename, data, sep=','):
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(sep.join(map(str, data)))