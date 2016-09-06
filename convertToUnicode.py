from io import open
import argparse

# Create the argument parser and populate with the arguments
parser = argparse.ArgumentParser(description='Convert from ISO-8859-9 to UTF-8')
parser.add_argument('--input', '-i', required=True)
parser.add_argument('--output', '-o', required=True)
args = parser.parse_args()

reader = args.input
writer = args.output

writeFile = open(writer, 'w')

with open(reader, encoding='ISO-8859-9') as fp:
	for line in fp:
		writeFile.write(line)

