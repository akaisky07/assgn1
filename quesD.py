from sklearn.decomposition import TruncatedSVD

def reduce_dimensionality(co_occurrence_matrix, k=2):
    svd = TruncatedSVD(n_components=k)
    embeddings = svd.fit_transform(co_occurrence_matrix)
    return embeddings

# Example usage:
# reduced_embeddings = reduce_dimensionality(co_matrix)

