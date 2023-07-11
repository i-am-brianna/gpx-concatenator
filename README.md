# GPX Concatenator

GPX Concatenator is a Python project that provides a set of scripts for concatenating and colorizing GPX (GPS Exchange Format) files.

## Files

The project consists of the following files:

1. **gpx_concatenator.py**: This file contains the `GPXConcatenator` class, responsible for concatenating multiple GPX files. It takes a list of input file paths, an output file path, and optional flags to enable metadata and colorization. The `concatenate_files` method extracts tracks from the input files using the `GPXFile` class and appends them to the output GPX file's XML structure. If colorization is enabled, the `GPXColorizer` class assigns distinct colors to the tracks and adds color metadata to the GPX file.

2. **gpx_colorizer.py**: This file contains the `GPXColorizer` class, which colorizes tracks in a GPX file. It assigns distinct colors to each track based on its name and adds color information to the GPX file's XML structure.

3. **gpx_file.py**: This file contains the `GPXFile` class, providing methods for working with individual GPX files. It initializes with a file path, parses the GPX file's XML structure, and extracts metadata and track elements.

4. **main.py**: This file serves as the entry point of the project. It demonstrates how to use the `GPXConcatenator` class to concatenate and colorize GPX files. The script initializes the `GPXConcatenator` class with input file paths, an output file path, and flags for metadata and colorization. The `concatenate_files` method performs the concatenation and colorization process.

## Installation

To install `gpx-concatenator`, you can use pip, the Python package manager. Open a terminal and run the following command:

```
pip install gpx-concatenator
```

## Usage

Once installed, you can use the `gpx-concatenator` command to concatenate and colorize GPX files. Here's an example usage:

```
gpx-concatenator -i <input-directory> -o <output-file-name> -m -c
```

Replace `<input-directory>` with the directory containing the input GPX files, and `<output-file-name>` with the desired name of the output GPX file. The `-m` flag enables metadata in the output file, and the `-c` flag enables coloring of the tracks.

### Command-line Arguments

The following command-line arguments are available:

- `-i, --input-dir`: Specifies the directory containing the input GPX files. The default value is `input`.

- `-o, --output-file`: Specifies the name of the output GPX file. The default value is `output.gpx`.

- `-m, --enable-metadata`: Enables metadata in the output GPX file. This is an optional flag.

- `-c, --enable-coloring`: Enables coloring of the tracks in the output GPX file. This is an optional flag.

For more information on available command-line arguments, use the `-h, --help` flag:

```
gpx-concatenator --help
```

### Input Files

Place the GPX files that you want to concatenate in the specified input directory. The files will be concatenated in alphabetical order based on their names.

### Output File

The concatenated GPX file will be created with the specified name in the current working directory. If the file already exists, it will be overwritten.

## License

This project is licensed under the MIT License.

     _                 _          _                         
    (_)               | |        (_)                        
     _  __ _ _ __ ___ | |__  _ __ _  __ _ _ __  _ __   __ _ 
    | |/ _` | '_ ` _ \| '_ \| '__| |/ _` | '_ \| '_ \ / _` |
    | | (_| | | | | | | |_) | |  | | (_| | | | | | | | (_| |
    |_|\__,_|_| |_| |_|_.__/|_|  |_|\__,_|_| |_|_| |_|\__,_|