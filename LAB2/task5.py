def get_vowels(words):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'а', 'у', 'о', 'ы', 'э', 'я', 'ю', 'ё', 'и', 'е']

    def vowel_in_word(word):
        return sum(char.lower() in vowels for char in word)

    return list(map(vowel_in_word, words))