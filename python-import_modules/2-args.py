#!/usr/bin/python3
from sys import argv

argc = len(argv) - 1

if argc == 0:
    print("0 arguments.")
else:
    print("{} argument{}:".format(argc, "s" if argc != 1 else ""))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
