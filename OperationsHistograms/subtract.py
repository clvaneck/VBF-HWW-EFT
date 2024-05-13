import yoda
import argparse
import operator

## The syntax to use this is: python subtract.py file1 file2 -o output_file
## This code is used to subtract two yoda files (two histograms). The output file is the file where the result will be stored.

def subtract_yoda_files(files, output_file):
    # Load the first file
    result_histo = yoda.read(files[0])

    # Subtract the rest of the files
    for file in files[1:]:
        histo = yoda.read(file)
        for key, value in histo.items():
            if type(value) == yoda.core.Scatter1D:
                continue
            result_histo[key] = operator.sub(result_histo[key], histo[key])

    # Write the result to the output file
    yoda.write(result_histo, output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Subtract YODA files.')
    parser.add_argument('files', nargs='+', help='The YODA files to subtract')
    parser.add_argument('-o', '--output', help='The output file', required=True)

    args = parser.parse_args()

    subtract_yoda_files(args.files, args.output)