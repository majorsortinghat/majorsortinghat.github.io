# -*- coding: UTF-8 -*-

import sys

def main():
    if len(sys.argv) < 1:
        print("you must call with the name of the file, excluding \".csv\"")
        sys.exit(1)
    file_name = sys.argv[1]

    with open(file_name + '.csv', encoding='utf-8') as read_file, open(file_name + "_real.csv", 'w', encoding='utf-8') as write_file:
        for read_line in read_file:
            write_file.write(read_line.replace('\t', ','))
            print(read_line.replace('\t', ','))

if __name__ == "__main__":
    main()