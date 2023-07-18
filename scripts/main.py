import os
import argparse
from gpx_concatenator.gpx_concatenator import GPXConcatenator
import argcomplete

def main():
    # Create an argument parser
    parser = argparse.ArgumentParser(description='GPX Concatenator')
    parser.add_argument('-i', '--input-dir', default='input', help='Directory containing input files').completer = argcomplete.completers.DirectoriesCompleter()
    parser.add_argument('-o', '--output-file', default='output.gpx', help='Output file name', type=argparse.FileType('w'))
    parser.add_argument('-m', '--enable-metadata', action='store_true', help='Enable metadata in the output file')
    parser.add_argument('-c', '--enable-coloring', action='store_true', help='Enable coloring in the output file')

    # Activate autocompletion for paths
    argcomplete.autocomplete(parser)

    # Parse the command-line arguments
    args = parser.parse_args()

    # Get the input files from the specified directory
    input_files = sorted([os.path.join(args.input_dir, file) for file in os.listdir(args.input_dir) if file.endswith('.gpx')])

    # Create an instance of GPXConcatenator with the specified parameters
    concatenator = GPXConcatenator(
        input_files,
        args.output_file.name,
        enable_metadata=args.enable_metadata,
        enable_coloring=args.enable_coloring
    )

    # Concatenate the files
    concatenator.concatenate_files()

if __name__ == '__main__':
    main()
