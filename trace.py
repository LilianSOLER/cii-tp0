#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from math import *


def trace(function, xmin, xmax, nstep, output):
    output.write("x, %s\n" % function)
    function = eval("lambda x:" + function)
    
    step = 1.*(xmax-xmin)/nstep
    for i in range(nstep+1):
        x = xmin + i*step
        try:
            y = function(x)
        except:
            continue
        output.write("%s, %s\n" % (x, y))


def main(argv=None):
    if argv is None:
        argv = sys.argv
    
    import getopt
    try:
        options, argv = getopt.getopt(argv[1:], "o:", ["output="])
    except getopt.GetoptError as message:
        sys.stderr.write("%s\n" % message)
        sys.exit(1)
    
    if len(argv) != 1:
        sys.exit(1)
    function = argv[0]
    
    output = sys.stdout
    xmin, xmax = 0., 1.
    nstep = 10
    
    for option, value in options:
        if option in ["-o", "--output"]:
            output = open(value, "w")
        else:
            assert False, "unhandled option"
    
    trace(function, xmin, xmax, nstep, output)


if __name__ == "__main__":
    sys.exit(main())
