#!/usr/bin/python3
from PyPDF2 import PdfReader, PdfFileMerger
from pathlib import Path

import argparse
import os

def pdf_handler():
    parser = argparse.ArgumentParser(description="Exercises PDF modification \
        functionality.")
    parser.add_argument('-d', '--directory', metavar="PATH", type=str, help=" \
    Path to a directory in which all PDFs will be sequentially merged")
    parser.add_argument('-o', '--output', metavar="PATH", type=str,
    default="output.pdf", help="Path to resultant file")

    args = parser.parse_args()

    merger = PdfFileMerger()

    for file in os.listdir(args.directory):
        file_path = os.path.join(args.directory, file)
        if file_path.endswith(".pdf"):
            merger.append(file_path)
    
    with open((args.output), 'wb') as fileobj:
        merger.write(fileobj)

    print("Successfully wrote resultant PDF to " + args.output)

    merger.close()


if __name__ == "__main__":
    pdf_handler()

