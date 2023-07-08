# GPX File Concatenator

This project provides a set of Python scripts for concatenating and colorizing GPX (GPS Exchange Format) files. It allows you to combine multiple GPX files into a single output file and optionally add colorization to the tracks.

## Files

The project consists of the following files:

1. **gpx_concatenator.py**: This file contains the `GPXConcatenator` class, which handles the concatenation of multiple GPX files. It takes a list of input file paths, an output file path, and optional flags to enable metadata and colorization. The `concatenate_files` method iterates over the input files, extracts the tracks using the `GPXFile` class, and appends them to the output GPX file's XML structure. If colorization is enabled, it utilizes the `GPXColorizer` class to assign colors to the tracks and add color metadata to the GPX file.

2. **gpx_colorizer.py**: This file contains the `GPXColorizer` class, which is responsible for colorizing tracks in a GPX file. It provides methods for assigning distinct colors to each track based on its name. The `_generate_distinct_colors` method generates a list of distinct colors based on the number of tracks. The `_add_color_extensions` method adds color information to the GPX file's XML structure, and the `colorize_tracks` method applies colorization to the tracks.

3. **gpx_file.py**: This file contains the `GPXFile` class, which provides methods for working with individual GPX files. The `__init__` method initializes the class with a file path and parses the XML structure of the GPX file. The `extract_metadata` method extracts the metadata element from the GPX file's XML structure, and the `extract_tracks` method extracts a list of track elements from the XML structure.

4. **main.py**: This file serves as the entry point of the project. It demonstrates how to use the `GPXConcatenator` class to concatenate and colorize GPX files. The script initializes the `GPXConcatenator` class with a list of input file paths, an output file path, and flags to enable metadata and colorization. It then calls the `concatenate_files` method to perform the concatenation and colorization process.

## Usage

To use this project, follow these steps:

1. Place the GPX files that you want to concatenate in the `input` directory or specify a different input directory using the `--input-dir` command-line parameter.

2. Run the `main.py` script using a Python interpreter and specify the desired command-line parameters. Here are some examples:

   ```shell
   # Run the script with default parameters
   python main.py

   # Specify a different input directory
   python main.py --input-dir my_input_dir

   # Specify a different output file name
   python main.py --output-file my_output.gpx

   # Enable metadata and coloring
   python main.py --enable-metadata --enable-coloring
The concatenated and colorized GPX file will be generated based on the specified parameters.

## Requirements

- Python 3.x
- The following Python packages: `xml.etree.ElementTree`, `xml.dom.minidom`

## Disclaimer

This project is provided as-is without any warranty. Use it at your own risk.

Please ensure that you have the necessary permissions and rights to use the GPX files you provide as input.

## Contributions

Contributions to this project are welcome! If you find any issues or have ideas for improvements, feel free to submit a pull request or open an issue.

We appreciate your feedback and contributions to make this project better.


     _                 _          _                         
    (_)               | |        (_)                        
     _  __ _ _ __ ___ | |__  _ __ _  __ _ _ __  _ __   __ _ 
    | |/ _` | '_ ` _ \| '_ \| '__| |/ _` | '_ \| '_ \ / _` |
    | | (_| | | | | | | |_) | |  | | (_| | | | | | | | (_| |
    |_|\__,_|_| |_| |_|_.__/|_|  |_|\__,_|_| |_|_| |_|\__,_|
                                                        
                                                        