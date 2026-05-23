import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """

    arr = np.asarray(x, dtype = float)
    # Write code here
    return np.maximum(0, arr)
    