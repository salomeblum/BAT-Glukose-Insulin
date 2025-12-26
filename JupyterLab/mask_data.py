import numpy as np

def mask_data(t1:np.ndarray, t2:np.ndarray, data:np.ndarray) -> np.ndarray:
    """ len(t1) == len(data)
        len(t1) > len(t2)
    """
    mask = np.isin(t1, t2)
    data_new = data[mask]
    return data_new