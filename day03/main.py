def get_file_lines(filename: str):
    with open(filename) as file:
        return file.read().splitlines()


def get_digit_counts(l: list(), idx: int) -> tuple(int, int):
    ones_count = sum([int(number[idx]) for number in l])
    zeros_count = len(l) - ones_count
    return ones_count, zeros_count


def main():
    lines = get_file_lines('day03/input.txt')

    ogr = csr = lines

    for i in range(len(lines[0])):

        if len(ogr) > 1:
            ones_count, zeros_count = get_digit_counts(ogr, i)
            ogr = [number for number in ogr if number[i] ==
                   ('1' if ones_count >= zeros_count else '0')]
        if len(csr) > 1:
            ones_count, zeros_count = get_digit_counts(csr, i)
            zeros_count = len(csr) - ones_count
            csr = [number for number in csr if number[i] ==
                   ('1' if ones_count < zeros_count else '0')]

    print(int(ogr[0], 2) * int(csr[0], 2))


if __name__ == '__main__':
    main()
