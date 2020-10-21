import numpy as np

def compute_r_squared(data, predictions):
    # Write a function that, given two input numpy arrays, 'data', and 'predictions,'
    # returns the coefficient of determination, R^2, for the model that produced 
    # predictions.
    # 
    # Numpy has a couple of functions -- np.mean() and np.sum() --
    # that you might find useful, but you don't have to use them.

    # YOUR CODE GOES HERE

    numerator = ((data-predictions)**2).sum()
    denominator = ((data-np.mean(data))**2).sum()
    
    r_squared = 1 - numerator / denominator

    return r_squared