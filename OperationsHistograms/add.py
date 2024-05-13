import yoda
import argparse

## The syntax to use this is: python add.py file1 file2 -o output_file
## This code is used to add two yoda files (two histograms). The output file is the file where the result will be stored.


##Loading the files

def add_yoda_files(file1,file2,output_file):

    histo1 = yoda.read(file1)
    histo2 = yoda.read(file2)

    ## Perform the addition
    result_histo={}

    for key, value in histo1.items():
        if type(value)==yoda.core.Scatter1D:
            continue
        result_histo[key]= histo1[key] + histo2[key]

    yoda.core.write(result_histo, output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Add two YODA files.')
    parser.add_argument('file1', help='The first YODA file')
    parser.add_argument('file2', help='The second YODA file')
    parser.add_argument('-o', '--output', help='The output file', required=True)

    args = parser.parse_args()

    add_yoda_files(args.file1, args.file2, args.output)