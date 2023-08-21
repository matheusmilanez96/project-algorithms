def is_palindrome_recursive_aux(word, low_index, high_index):
    if low_index == high_index:
        return word[0]
    else:
        new_word = word[high_index] + is_palindrome_recursive_aux(
            word, low_index, high_index - 1)
        return new_word


def is_palindrome_recursive(word, low_index, high_index):
    if word is None or len(word) == 0:
        return False
    if low_index == high_index:
        return True
    new_word = word[high_index] + is_palindrome_recursive_aux(
        word, low_index, high_index - 1)
    return new_word == word


print(is_palindrome_recursive("", 0, 0))
