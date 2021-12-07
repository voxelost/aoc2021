def get_file_lines(filename: str):
    with open(filename) as file:
        return file.read().splitlines()


def main():
    lines = get_file_lines('day01/input.txt')

    MASK_SIZE = 3

    last = sum([int(i) for i in lines[0:MASK_SIZE]])
    counter = 0

    for x, _ in enumerate(lines[:1 - MASK_SIZE]):
        curr = sum([int(i) for i in lines[x:x + MASK_SIZE]])
        if curr > last:
            counter += 1

        last = curr

    print(counter)


if __name__ == '__main__':
    main()
