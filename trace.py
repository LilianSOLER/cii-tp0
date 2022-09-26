#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from math import *


def trace(function, xmin, xmax, nstep, output):
    output.write("x, %s\n" % function)
    function = eval("lambda x:" + function)

    step = 1. * (xmax - xmin) / nstep
    for i in range(nstep + 1):
        x = xmin + i * step
        try:
            y = function(x)
        except:
            continue
        output.write("%s, %s\n" % (x, y))


def usage():
    from textwrap import dedent
    txt = """\
    usage: %s [options] function
    options:
        -h, --help: print this help
        -o, --output: output file
        -x, --xmin: minimum value of x
        -X, --xmax: maximum value of x
        """
    sys.stderr.write(dedent(txt))


def main(argv=None):
    if argv is None:
        argv = sys.argv

    import getopt
    try:
        options, argv = getopt.getopt(argv[1:], "ho:x:X:", ["help", "output=", "xmin=", "xmax="])
    except getopt.GetoptError as message:
        sys.stderr.write("%s\n" % message)
        sys.stderr.write("use -h for help\n")
        sys.exit(1)


    output = sys.stdout
    xmin, xmax = 0., 1.
    nstep = 10

    for option, value in options:
        print("option: " + option)
        print("value: " + value)
        if option in ("-h", "--help"):
            usage()
            sys.exit(0)
        elif option in ["-o", "--output"]:
            output = open(value, "w")
        elif option in ["-x", "--xmin"]:
            xmin = float(value)
        elif option in ["-X", "--xmax"]:
            xmax = float(value)
        else:
            assert False, "unhandled option"

    if len(argv) != 1:
        sys.stderr.write("use -h for help\n")
        sys.exit(1)

    function = argv[0]

    trace(function, xmin, xmax, nstep, output)


if __name__ == "__main__":
    sys.exit(main())
