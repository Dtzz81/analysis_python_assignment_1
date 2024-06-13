import numpy as np
from dev_calc.mean_var_std import calculate

def test_min_max_sum():


    matrix = np.array([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]])

    expected = calculate(matrix)

    assert expected['min'] == np.min(matrix)
    assert expected['max'] == np.max(matrix)
    assert expected['sum'] == np.sum(matrix)

print("It appeared" + letter + "times.")
#
