#!/usr/bin/python3
from PyPDF2 import PdfReader, PdfFileMerger

import argparse
import os

def pdf_handler():
    parser = argparse.ArgumentParser(description="Exercises PDF modification \
        functionality.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-d', '--directory', metavar="PATH", type=str, help=" \
    Path to a directory in which all PDFs will be sequentially merged")
    group.add_argument('-f', '--files', metavar="PATH", type=str, nargs='+',
    help="Paths to two or more PDFs to merge.")
    parser.add_argument('-o', '--output', metavar="PATH", type=str,
    default="output.pdf", help="Path to resultant file. Default will be \
     \"output.pdf\" in your current directory. ")

    args = parser.parse_args()

    merger = PdfFileMerger()

    if args.directory:
        for file in os.listdir(args.directory):
            file_path = os.path.join(args.directory, file)
            if file_path.endswith(".pdf"):
                merger.append(file_path)
    
    if args.files:
        for file_path in args.files:
            merger.append(file_path)
    
    with open((args.output), 'wb') as fileobj:
        merger.write(fileobj)

    print("Successfully wrote resultant PDF to " + args.output)

    merger.close()


if __name__ == "__main__":
    pdf_handler()

