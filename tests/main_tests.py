from main import create_mine_field, is_mine


def test_create_mine_field():
    field = create_mine_field()
    assert isinstance(field, list)


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
