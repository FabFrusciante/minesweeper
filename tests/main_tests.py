from main import create_mine_field, is_mine


def test_create_mine_field():
    field = create_mine_field()
    assert field is not None
    assert isinstance(field, dict)
    print(len(field))
    assert len(field) == 64
    for value in field.values():
        if value not in [0, 1]:
            assert False


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
