def co_occurrence_matrix(corpus, vocab, window_size=4):
    vocab_size = len(vocab)
    co_occurrence = np.zeros((vocab_size, vocab_size))

    for sentence in corpus:
        words = sentence.split()
        for i, word in enumerate(words):
            center_index = vocab.index(word)
            start = max(0, i - window_size)
            end = min(len(words), i + window_size + 1)
            context = words[start:i] + words[i + 1:end]
            for context_word in context:
                if context_word in vocab:
                    context_index = vocab.index(context_word)
                    co_occurrence[center_index][context_index] += 1

    return co_occurrence

# Example usage:
# co_matrix = co_occurrence_matrix(corpus, distinct_words)

