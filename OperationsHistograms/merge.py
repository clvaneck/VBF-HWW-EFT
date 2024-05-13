import yoda
import argparse

## The syntax to use this is: python merge.py file1 file2 -o output_file
## This code is used to merge two yoda files (two histograms) into one output file where both can be viewed distinctly.

def merge_yoda_files(file1, file2, output_file):
    # Read the YODA files
    histo1 = yoda.read(file1)
    histo2 = yoda.read(file2)

    # Prepare the result dictionary
    result_histo = {}

    # Prefix for distinguishing histograms from each file
    prefix1 = "file1_"
    prefix2 = "file2_"

    # Process the first file histograms
    for key, value in histo1.items():
        new_key = prefix1 + key  # Create a new key with prefix
        result_histo[new_key] = value  # Assign the histogram to the new key

    # Process the second file histograms
    for key, value in histo2.items():
        new_key = prefix2 + key  # Create a new key with prefix
        result_histo[new_key] = value  # Assign the histogram to the new key

    # Write the combined histograms to the output file
    yoda.write(result_histo, output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Merge two YODA files into one.')
    parser.add_argument('file1', help='The first YODA file')
    parser.add_argument('file2', help='The second YODA file')
    parser.add_argument('-o', '--output', help='The output file', required=True)

    args = parser.parse_args()

    merge_yoda_files(args.file1, args.file2, args.output)
