"""Testing non_normal.fleishman"""

import numpy as np

from non_normal import fleishman


def test_fl_coeff_vsk():
    """Test the Fleishman.fl_coeff_vsk method"""

    ff = fleishman.Fleishman()

    assert ff.fl_coeff_vsk(1, 2, 3) == (162, 4080, 601248)


def test_fl_func():
    """Test the Fleishman.fl_func method"""

    ff = fleishman.Fleishman()

    assert ff.fl_func(1, 2, 3) == (161, 4080, 601248)


def test_fl_deriv():
    """Test the Fleishman.fl_deriv method"""

    ff = fleishman.Fleishman()

    expected_mat = np.array([[20, 8, 96], [296, 2040, 2616], [39432, 130080, 699960]])

    output_mat = ff.fl_deriv(1, 2, 3)
    assert np.all(expected_mat == output_mat)


def test_newton():
    """Test the Fleishman.newton method"""

    ff = fleishman.Fleishman()

    assert ff.newton(1, 10, 100) == (1.4943510437111611, 0.0, -0.21450355527308587)


def test_fl_ic():
    """Test the Fleishman.fl_ic method"""

    ff = fleishman.Fleishman()

    assert ff.fl_ic() == (0.95357, 0.0, 0.007927416500000006)


def test_gen_field_values():
    """Test the Fleishman.gen_field.field attribute

    For default input params with size=4
    """

    ff = fleishman.Fleishman(size=4)
    ff.gen_field()

    expected = np.array([0.30471708, -1.03998411, 0.7504512, 0.94056472])
    assert np.all(np.isclose(expected, ff.field))


def test_gen_field_stats():
    """Test the Fleishman.gen_field.field_stats attribute

    For default input params with size=4
    """

    ff = fleishman.Fleishman(size=4)
    ff.gen_field()
    stats = ff.field_stats

    expected = {
        "mean": 0.23893722142790175,
        "var": 0.5984736099498982,
        "skew": -0.8706188765823788,
        "ekurt": -0.9157032449998184,
    }

    assert {expected == stats}


def test_gen_field_value_err():
    """Test the Fleishman.gen_field ValueError

    For default input params with size=4
    """

    try:
        ff = fleishman.Fleishman(skew=2, ekurt=5, size=4)
        ff.gen_field()

    except ValueError:
        assert True
