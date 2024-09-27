import numpy as np

def convert_numpy_float32_to_float(d):
    if isinstance(d, dict):
        return {k: convert_numpy_float32_to_float(v) for k, v in d.items()}
    elif isinstance(d, list):
        return [convert_numpy_float32_to_float(item) for item in d]
    elif isinstance(d, np.float32):
        return float(d)
    else:
        return d