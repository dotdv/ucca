#!/usr/bin/python3

import argparse
import os
import sys

from parsing import util, perceptron

desc = """Reads a model file in pickle format and writes as TSV
"""


def main():
    argparser = argparse.ArgumentParser(description=desc)
    argparser.add_argument('infile', help="binary model file to read")
    argparser.add_argument('outfile', nargs="?", help="tsv file to write (if missing, <infile>.tsv)")
    args = argparser.parse_args()

    model = perceptron.Perceptron()
    model.load(args.infile, util)
    model.write(args.outfile or os.path.splitext(args.infile)[0] + ".tsv")

    sys.exit(0)


if __name__ == '__main__':
    main()
