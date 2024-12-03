
from include.Win_Func import list_directories
import argparse  ## to import values from command line.

## Call Format  <python Main.py "C:\\Users\\Metac\\">
## Setting up argument parser
parser = argparse.ArgumentParser(description="Listing Directories")
## Add argument for the path 
parser.add_argument("path",type=str,help="Directory path")
# Parse the arguments
args = parser.parse_args()
directories = list_directories(args.path)
print(directories)