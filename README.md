# PyDF

## Description

A simple command line interface for merging PDF files leveraging the PyPDF2 library.

## Installation

This project requires that you have Python 3 and pipenv installed on your machine.

Clone the repository and then execute a `pipenv install` to acquire all necessary packages.

## Usage

1. Activate the pipenv virtual environment through `pipenv shell`. This shell can be quit at any time by entering the `exit` command.

2. Execute `python3 PyDF.py -h` to view all availabe commands. The supported commands currently are:
    * `-h, --help` prints the description of the program and all valid commands before exiting.
    * `-d, --directory` takes a path (absolute or relative) to a directory and sequentially merges all files with a `.pdf` extension in that directory.
    * `-f, --files` takes two or more paths to files with a `.pdf` extension and merges them.
    * `-o, --output` takes a path to the resultant merged file. The default path is `output.pdf` in your current directory.

## Examples

`python3 PyDF.py -f ../PDF_holder/1.pdf ../PDF_holder/2.pdf`

This command will merge `1.pdf` and `2.pdf` and place the resultant file `output.pdf` in your current directory.

-------------------------------------------

`python3 PyDF.py -d ../PDF_holder -o ../PDF_holder/my_merged_file.pdf`

This command will merge all `.pdf` files in the directory `PDF_holder` and generate a resultant file in the `PDF_holder` directory titled `my_merged_file.pdf`.

## License

This work is protected by the **GNU GPLv3** license.
