from main import create_mine_field


def test_create_mine_field():
    field = create_mine_field()
    assert field is not None
    assert isinstance(field, dict)
    print(len(field))
    assert len(field) == 64
    for value in field.values():
        if value not in [0, 1]:
            assert False
