#!/usr/bin/env python3
"""
This module prints the number of and the list of its arguments.
"""

if __name__ == "__main__":
    from sys import argv

    argc = len(argv) - 1

    if argc == 0:
        print("{:d} argument.".format(argc))
    elif argc == 1:
        print("{:d} argument:".format(argc))
    else:
        print("{:d} arguments:".format(argc))

    for i in range(1, argc + 1):
        print("{:d}: {}".format(i, argv[i]))
