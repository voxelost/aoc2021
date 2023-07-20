
def get_file_lines(filename: str):
    with open(filename) as file:
        return file.read().splitlines()


def multiply_list(l: list(), value) -> list():
    return [i * value for i in l]


def add_list(l: list(), other: list()) -> list():
    if len(l) > len(other):
        return []

    return [i + other[x] for x, i in enumerate(l)]


def get_list_for_direction(direction: str) -> list():
    if direction == 'up':
        return [-1, 0, 0]
    if direction == 'forward':
        return [0, 1, 1]
    if direction == 'down':
        return [1, 0, 0]

    return [0, 0, 0]


def main():
    lines = get_file_lines('day02/input.txt')

    current_pos = [0, 0]
    current_aim = 0

    for line in lines:
        direction, value = line.split()[0], int(line.split()[1])

        dir_list = get_list_for_direction(direction)

        current_pos[0] += dir_list[2] * value * current_aim  # y
        current_pos[1] += dir_list[2] * value  # x

        current_aim += dir_list[0] * value

    print(current_pos[0] * current_pos[1])


if __name__ == '__main__':
    main()
