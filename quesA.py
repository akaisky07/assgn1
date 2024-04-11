import numpy as np
import matplotlib.pyplot as plt

def plot_embeddings(embeddings, words):
    fig, ax = plt.subplots()
    for word, emb in zip(words, embeddings):
        ax.scatter(emb[0], emb[1])
        ax.annotate(word, (emb[0], emb[1]))
    plt.show()

# Example usage:
# embeddings = [[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]]
# words = ['word1', 'word2', 'word3']
# plot_embeddings(embeddings, words)

