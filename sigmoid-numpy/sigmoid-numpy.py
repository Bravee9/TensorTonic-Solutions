import numpy as np
import math

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    arr = np.asarray(x, dtype=float)
    return 1 / (1 + np.exp(-arr))