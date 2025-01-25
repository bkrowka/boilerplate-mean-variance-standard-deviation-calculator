import numpy as np

def calculate(list):
        if len(list) != 9:
                return ValueError("List must contain nine numbers.")
        array = np.array(list).reshape(3, 3)
        mean = [np.mean(array, axis=0).tolist(), np.mean(array, axis=1).tolist(), np.mean(array)]
        calculations = {}
        calculations["mean"] = mean
        return calculations
