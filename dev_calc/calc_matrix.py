import numpy as np

def calculate(matrix_list):

    matrix = np.array([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]])


    # Convert the list to a 3x3 NumPy array
    matrix = np.array(matrix_list).reshape(3, 3)


    statistics = {
        'mean': {
            'row': np.mean(matrix, axis=1).tolist(),
            'column': np.mean(matrix, axis=0).tolist(),
            'flattened': np.mean(matrix),
        },
        'variance': {
            'row': np.var(matrix, axis=1).tolist(),
            'column': np.var(matrix, axis=0).tolist(),
            'flattened': np.var(matrix),
        },
        'std_deviation': {
            'row': np.std(matrix, axis=1).tolist(),
            'column': np.std(matrix, axis=0).tolist(),
            'flattened': np.std(matrix),
        },
        'max': {
            'row': np.max(matrix, axis=1).tolist(),
            'column': np.max(matrix, axis=0).tolist(),
            'flattened': np.max(matrix),
        },
        'min': {
            'row': np.min(matrix, axis=1).tolist(),
            'column': np.min(matrix, axis=0).tolist(),
            'flattened': np.min(matrix),
        },
        'sum': {
            'row': np.sum(matrix, axis=1).tolist(),
            'column': np.sum(matrix, axis=0).tolist(),
            'flattened': np.sum(matrix),
        },
    }

    return statistics


