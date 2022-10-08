#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from math import *

def trace(function, xmin, xmax, nstep, output):
    print(output.name)
    tpm = output.name.split(".")
    print(tpm)
    if(tpm[1] != "ps"):
        output.write("x, %s\n" % function)
    else :
        output.write("%!\nnewpath\n100 600 moveto\n(" + str(xmin) + ") show\n0 -400 rlineto\n(" + str(xmax) + ") show\nclosepath\n400 0 rlineto\nclosepath\n")

    function = eval("lambda x:" + function)


    oldy = 0

    step = (xmax - xmin) / nstep
    for i in range(nstep + 1):
        x = xmin + i * step
        try:
            y = function(x)
        except:
            continue

        if(tpm[1] != "ps"):
            output.write("x, %s\n" % function)
        else :
            output.write("%s %s rlineto\n" % (200/nstep, -(oldy-y)*200))
            #output.write("%s %s lineto\n" % ((200)+x*(200/xmax), 200+y*200))
            #output.write("%s %s lineto\n" % ((200)+x*(200/xmax), 200+y*200))
            oldy = y   
        
        #output.write("%s, %s\n" % (x, y))

    output.write("stroke\n")
    output.write("showpage\n")



def usage():
    from textwrap import dedent
    txt = """\
    usage: %s [options] function
    options:
        -h, --help: print this help
        -o, --output: output file
        -x, --xmin: minimum value of x
        -X, --xmax: maximum value of x
        -n, --nstep: number of step
        """
    sys.stderr.write(dedent(txt))


def main(argv=None):
    if argv is None:
        argv = sys.argv

    import getopt
    try:
        options, argv = getopt.getopt(argv[1:], "ho:x:X:n:", ["help", "output=", "xmin=", "xmax=", "nstep="])
    except getopt.GetoptError as message:
        sys.stderr.write("%s\n" % message)
        sys.stderr.write("use -h for help\n")
        sys.exit(1)


    output = sys.stdout
    xmin, xmax = 0., 1.
    nstep = 10

    for option, value in options:
        if option in ("-h", "--help"):
            usage()
            sys.exit(0)
        elif option in ["-o", "--output"]:
            output = open(value, "w")
        elif option in ["-x", "--xmin"]:
            xmin = float(value)
        elif option in ["-X", "--xmax"]:
            xmax = float(value)
        elif option in ["-n", "--nstep"]:
            nstep = int(value)
        else:
            assert False, "unhandled option"

    if len(argv) != 1:
        sys.stderr.write("use -h for help\n")
        sys.exit(1)

    function = argv[0]

    trace(function, xmin, xmax, nstep, output)


if __name__ == "__main__":
    sys.exit(main())