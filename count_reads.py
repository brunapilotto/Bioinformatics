import os
from termcolor import colored
import argparse


def menu():
    parser = argparse.ArgumentParser(description="Count reads from fastq \
                                                    files in a directory")
    parser.add_argument("--path",
                        required=True,
                        help="Path to the directory with fastq files")
    args = parser.parse_args()
    return args


def count_reads(file: str) -> int:
    with open(file, 'r') as f:
        lines = f.readlines()
        return int(len(lines) / 4)


def count_reads_in_directory(directory: str) -> None:
    files = [file for file in os.listdir(directory) if file.endswith('.fastq')]
    files.sort()
    for file in files:
        print(f"Arquivo {colored(file, 'green')} possui {colored((count_reads(os.path.join(directory, file))), 'green')} reads")


if __name__ == "__main__":
    options = menu()
    print(colored('Read count', 'magenta'))
    count_reads_in_directory(options.path)
