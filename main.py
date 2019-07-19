import argparse
import sys

from util import process_file

arg_parser = argparse.ArgumentParser(
    description="Scrape phone numbers from urls in file"
)
arg_parser.add_argument("file", metavar="file")
args = arg_parser.parse_args()

print(process_file(args.file))
