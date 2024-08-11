
def find_top_k_words(words: list[str], k: int):  # LeetCode Q.692.
    hash_table, frequency_table = dict(), dict()
    for word in words:
        if word not in hash_table.keys():
            hash_table.update({word: 1})
        hash_table[word] += 1

    for word, frequency in hash_table.items():
        if frequency not in frequency_table.keys():
            frequency_table.update({frequency: []})
        frequency_table[frequency].append(word)

    # Use frequency to collect words.
    top_k_words, frequency, collections = [], max(frequency_table.keys()), 0
    while True:
        frequency_table[frequency].sort()  # If frequency is equal, sort by alphabetical order.
        top_k_words.extend(frequency_table[frequency])
        collections += len(frequency_table[frequency])
        if collections >= k:
            return top_k_words[:k]

        frequency -= 1
        while frequency not in frequency_table.keys():
            frequency -= 1
