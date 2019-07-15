# Kennard-Stone-Algorithm

### Description
* Input: dataset with each row representing a sample; or (if precomputed=True) pairwise-distance matrix.
* Output: dataset containing selected samples; or (if precomputed=True) the index of selected samples.
* Dependency: numpy, scipy, pandas (required for precomputed=False), scikit-learn (optional) 

### Example

```python
from kenStone import *

# raw feature matrix
input = 'test/distArray.txt'
X = loadKS(input)
Y = kenStone(X, 10)
writeKS('test/KSfeatures.txt', Y)

# precomputed pairwise distance matrix
input = 'test/matrix.txt'
X = loadKS(input)
Y = kenStone(X, 10, precomputed=True)
writeKS('test/KSelected.txt', Y, precomputed=True)
```


### Algorithm
The text below was taken from: http://wiki.eigenvector.com/index.php?title=Kennardstone

> Select a subset of samples from a data set by the Kennard-Stone algorithm.

> The KENNARDSTONE method selects a subset of samples from x which provide uniform coverage over the data set and includes samples on the boundary of the data set. The method begins by finding the two samples which are farthest apart using geometric distance. To add another sample to the selection set the algorithm selects from the remaining samples that one which has the greatest separation distance from the selected samples. The separation distance of a candidate sample from the selected set is the distance from the candidate to its closest selected sample. This most separated sample is then added to the selection set and the process is repeated until the required number of samples, k, have been added to the selection set. In practice this produces a very uniformly distributed network of selected points over the data set and includes samples along the boundary of the dataset. The method performs efficiently because it calculates the inter-sample distances matrix only once.

> The method is implemented following the description published in R. W. Kennard & L. A. Stone (1969): Computer Aided Design of Experiments, Technometrics, 11:1, 137-148. https://www.tandfonline.com/doi/abs/10.1080/00401706.1969.10490666




