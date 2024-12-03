
from include.Win_Func import list_directories
import argparse  ## to import values from command line.

## 1. improvement to list down all subdirectories with full paths.
## 2. Return the List in formatted way like 1. path 2. path etc.
## 3. Call the Directory function only if asked by user input.
## 4. Next Function to List down all the files on path.

## Call Format  <python Main.py "C:\\Users\\Metac\\">
## Setting up argument parser
parser = argparse.ArgumentParser(description="Listing Directories")
## Add argument for the path 
parser.add_argument("path",type=str,help="Directory path")
# Parse the arguments
args = parser.parse_args()
directories = list_directories(args.path)
print(directories)