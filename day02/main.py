def get_file_lines(filename: str):
    with open(filename) as file:
        return file.read().splitlines()


def main():
    lines = get_file_lines('day02/test_input.txt')


if __name__ == '__main__':
    main()
