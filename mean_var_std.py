import numpy as np

def calculate(list):
        if len(list) != 9:
                return ValueError("List must contain nine numbers.")
        array = np.array(list).reshape(3, 3)
        mean = [np.mean(array, axis=0).tolist(), np.mean(array, axis=1).tolist(), np.mean(array)]
        variance = [np.var(array, axis=0).tolist(), np.var(array, axis=1).tolist(), np.var(array)]
        std_dev = [np.std(array, axis=0).tolist(), np.std(array, axis=1).tolist(), np.std(array)]
        calculations = {}
        calculations["mean"] = mean
        calculations["variance"] = variance
        calculations["standard deviation"] = std_dev
        return calculations
