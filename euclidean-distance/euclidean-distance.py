import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    """
    Returns the Euclidean distance as a Python float.
    """
    diff=np.asarray(x,dtype=float)-np.asarray(y,dtype=float)
    
    square_values=[ i**2 for i in diff ]
    res=np.sqrt(np.sum(square_values))
    return res