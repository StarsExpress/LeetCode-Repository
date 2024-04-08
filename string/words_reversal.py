
def reverse_words(string: str):  # LeetCode Q.151.
    words, reversed_words = string.split(' '), ''
    for i in range(len(words) - 1, -1, -1):
        word = words[i].strip()
        if len(word) > 0:
            reversed_words += f'{word} '  # Preserve a space as connection.
    return reversed_words.rstrip()
