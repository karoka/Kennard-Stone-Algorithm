
def skdist(X, precomputed=False):
    from sklearn import metrics
    if precomputed:
        return X
    return metrics.pairwise_distances(X, metric='euclidean', n_jobs=-1)

def scipydist(X, precomputed=False):
    from scipy.spatial import distance
    if precomputed:
        return X
    return distance.squareform(distance.pdist(X, metric='euclidean'))
