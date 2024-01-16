import numpy as np

def calculate(matrix):

    matrix = np.array([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]])

    result = {
        'mean': np.mean(matrix),
        'variance': np.var(matrix),
        'min': np.min(matrix),
        'max': np.max(matrix),
        'sum': np.sum(matrix),
    }

    return result
