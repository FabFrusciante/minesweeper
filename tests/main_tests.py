from main import create_mine_field, is_mine
import numpy as np


def test_create_mine_field():
    field = create_mine_field()
    assert isinstance(field, np.ndarray)
    assert (np.unique(field) == np.array([0, 1])).all()
    assert field.size == 64
    assert field.shape == (8, 8)


def test_is_mine():
    field = {(1, 2): 0}
    x = 1
    y = 2
    mine = is_mine(field, x, y)
    assert isinstance(mine, bool)
    assert mine is False

    field = {(1, 2): 1}
    mine = is_mine(field, x, y)
    assert mine is True
