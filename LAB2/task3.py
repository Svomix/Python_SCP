def get_palindrome(frequency_dict):
    return [key for key in frequency_dict if key == key[::-1]]
