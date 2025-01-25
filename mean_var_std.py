import numpy as np

def calculate(list):
        if len(list) != 9:
                raise ValueError("List must contain nine numbers.")
        array = np.array(list).reshape(3, 3)  # [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        # axis = 0 vertically
        # axis = 1 horizontally
        calculations = {
                "mean": [np.mean(array, axis=0).tolist(), np.mean(array, axis=1).tolist(), np.mean(array)],
                "variance": [np.var(array, axis=0).tolist(), np.var(array, axis=1).tolist(), np.var(array)],
                "standard deviation": [np.std(array, axis=0).tolist(), np.std(array, axis=1).tolist(), np.std(array)],
                "max": [np.max(array, axis=0).tolist(), np.max(array, axis=1).tolist(), np.max(array)],
                "min": [np.min(array, axis=0).tolist(), np.min(array, axis=1).tolist(), np.min(array)],
                "sum": [np.sum(array, axis=0).tolist(), np.sum(array, axis=1).tolist(), np.sum(array)]
        }
        return calculations
