#!/bin/bash

mkdir aoc2021
cd aoc2021

python3 -m venv venv
source venv/bin/activate

for day_no in {01..25} ; do
    mkdir day$day_no
    touch day$day_no/{input.txt,test_input.txt,main.py}
    echo "
    def get_file_lines(filename: str):
        with open(filename) as file:
        return file.read().splitlines()

    def main():
        lines = get_file_lines('day$day_no/input.txt')

    if __name__ == '__main__':
        main()
    " > day$day_no/main.py ;
done

git init --quiet

echo "
*/*input.txt
venv
" > .gitignore

