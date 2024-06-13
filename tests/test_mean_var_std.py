import numpy as np
from dev_calc.mean_var_std import calculate

#[x]Create a function named calculate() in mean_var_std.py
#[x] that uses Numpy to output the mean, variance, standard deviation, max, min, and sum of the rows,
#[x] columns, and elements in a 3 x 3 matrix.

def test_mean():

    matrix = np.array([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]])

    expected = calculate(matrix)
    assert expected['mean'] == np.mean(matrix)

def test_variance():

    matrix = np.array([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]])

    expected = calculate(matrix)
    assert expected['variance'] == np.var(matrix)

def test_min_max_sum():

    matrix = np.array([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]])

    expected = calculate(matrix)

    assert expected['min'] == np.min(matrix)
    assert expected['max'] == np.max(matrix)
    assert expected['sum'] == np.sum(matrix)

