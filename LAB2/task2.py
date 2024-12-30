def get_frequency(words: list[str]):
    return {word: words.count(word) for word in set(words)}
