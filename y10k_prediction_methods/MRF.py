import sys
from y10k_prediction_methods.dependence import *

from limix.ensemble.lmm_forest import  Forest as LMF
from limix.ensemble import lmm_forest_utils as utils

def mixed_forest_predictions(Y, which_col, X, K, Itrain, Itest, conditional=False, **kwargs):
    y = Y[:, which_col]
    if conditional:
        for j in range(Y.shape[1]):
            if j != which_col:
                X = np.column_stack((X, Y[:, j]))

    lm_forest = LMF(kernel=K[Itrain, :][:, Itrain], **kwargs)
    lm_forest.fit(X[Itrain, :], y[Itrain])
    predictions = lm_forest.predict(X[Itest, :], K[Itest, :][:, Itrain])

    return predictions
