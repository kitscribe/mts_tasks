#!/usr/bin/env python3
from classes import CustomFile
import os
import sys


def get_data(path: [str, os.PathLike]) -> dict:
    """
    Parse all files into the given folder and return a dict
    of the form {<round_size>: tuple(<files_count>, [<files extensions>])}

    :param path: absolute path to the folder
    :return: dict {<round_size>: tuple(<files_count>, [<files extensions>])}

    Example:
    python3 main.py "/home/<username>/test"

    is equivalent to
    ./main.py <given_path>

    Result:
    {3300: (1, ['.txt']), 100: (10, ['.xml', '.json', '.txt'])}
    """

    if not os.path.exists(path):
        raise ValueError(f"No such folder: {path}")

    result = dict()
    absolute_path = os.path.abspath(path)

    # get all files into the folder
    files = [CustomFile(os.path.join(absolute_path, file)) for file in os.listdir(absolute_path)
             if os.path.isfile(os.path.join(absolute_path, file))]

    # go through the files, get extensions and rounded sizes
    for file in files:
        if file.size not in result:
            result[file.size] = [file.extension]
        else:
            result[file.size] += [file.extension]

    # prepare data to output form
    for k, v in result.items():
        result[k] = (len(v), list(set(v)))

    return result


def main():
    if len(sys.argv) < 2:
        raise AttributeError("No path given")

    data = get_data(sys.argv[1])
    print(data)


if __name__ == '__main__':
    main()
