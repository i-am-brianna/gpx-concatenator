import os
from gpx_concatenator import GPXConcatenator


input_files = sorted([os.path.join("input", file) for file in os.listdir("input")])
output_file = "output.gpx"

concatenator = GPXConcatenator(input_files, output_file, enable_metadata=True, enable_coloring=True)
concatenator.concatenate_files()
