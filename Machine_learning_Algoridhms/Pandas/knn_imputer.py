from sklearn.impute import KNNImputer
import numpy as np

X = [ [3, np.NaN, 5], [1, 0, 0], [3, 3, 3] ]
print("X: ", X)
print("===========")


imputer = KNNImputer(n_neighbors= 1)
impute_with_1 = imputer.fit_transform(X)

print("\nImpute with 1 Neighbour: \n", impute_with_1)



imputer = KNNImputer(n_neighbors= 2)
impute_with_2 = imputer.fit_transform(X)

print("\n Impute with 2 Neighbours: \n", impute_with_2)