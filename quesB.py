def get_distinct_words(corpus):
    words = set()
    for sentence in corpus:
        for word in sentence.split():
            words.add(word)
    return list(words)

# Example usage:
# distinct_words = get_distinct_words(corpus)

