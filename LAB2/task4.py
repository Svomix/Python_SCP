def get_combination(words):
    result = [set()]
    for word in words:
        combinations = [comb | {word} for comb in result]
        result.extend(combinations)
    return result
