
import pandas as pd
import glob
import os
from datetime import datetime

# import required functions 
from include.Functions import go_to_cwd , mv

# Changing path to current working directory 
script_path = os.path.abspath(__file__)
go_to_cwd(script_path)

# Source Files path 
output_path=fr'{os.getcwd()}\data\output'


file_pattern = os.path.join(f'{output_path}', '*.csv')
all_files=glob.glob(file_pattern)

# print all file names 
file_names = [os.path.basename(file) for file in all_files]
for file in file_names:
    print(file)

# List to hold DataFrames
dataframes = []
 
# Loop through the list of files and read each file
for filename in all_files:
    df = pd.read_csv(filename)
    dataframes.append(df)

# Concatenate all DataFrames
merged_df = pd.concat(dataframes, ignore_index=True)

# downloading the final dataframe and creating an output file in output directory
timestamp=f'{datetime.now().strftime("%Y%m%d%H%M%S")}'
output_file_name=f"merged_output_{timestamp}.csv"
output_file_path=fr'{output_path}\{output_file_name}'
merged_df.to_csv(output_file_path, index=False)


