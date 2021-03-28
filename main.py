from random import randint
import numpy as np

field_size = 8


def create_mine_field():
    mine_field = np.array([randint(0, 1) for _ in range(0, field_size ** 2)])
    return mine_field.reshape(field_size, field_size)


def create_visual():
    visual = np.array(["x" for _ in range(0, field_size ** 2)])
    return visual.reshape(field_size, field_size)


def print_visual(visual: np.ndarray):
    for x in range(0, field_size):
        for y in range(0, field_size):
            print(visual[x, y], " ", end="")
        print("")


def is_mine(field: np.ndarray, x: int, y: int) -> bool:
    if field[x, y] == 0:
        return False
    return True


def update_visual(visual: np.ndarray, x: int, y: int) -> None:
    visual[x, y] = 0


def main():
    mine_field = create_mine_field()
    visual = create_visual()

    while True:
        print_visual(visual)
        x = int(input("x Koordinate: "))
        y = int(input("y Koordinate: "))

        if is_mine(mine_field, x, y):
            print("Mine. Spiel ist vorbei.")
            break
        print("Nichts")
        update_visual(visual, x, y)


if __name__ == '__main__':
    main()
