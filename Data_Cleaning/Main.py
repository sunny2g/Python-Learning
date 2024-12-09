
import pandas as pd 
import glob
import os
from datetime import datetime
import shutil

# import required functions 
from include.Functions import go_to_cwd , mv

## Optimization Steps 
# create small functions for each step and pull them from function file 
# Add try blocks to deal with errors 
# Add proper print messages for each step completion 
# extract remaining unformated data and add it in final dataframe 


# Changing path to current working directory 
script_path = os.path.abspath(__file__)
go_to_cwd(script_path)

# setting up Path Variables 
incoming_path=fr'{os.getcwd()}\data\incoming'
processing_path=fr'{os.getcwd()}\data\processing'
archive_path=fr'{os.getcwd()}\data\archive'
output_path=fr'{os.getcwd()}\data\output'



# Identifying all the files 
file_pattern = os.path.join(f'{incoming_path}', '*.csv')
all_incoming_files=glob.glob(file_pattern)
file_names = [os.path.basename(file) for file in all_incoming_files]
for file in file_names:
    # Moving csv files to processing path 
    source_path=fr'{incoming_path}\{file}'
    target_path=fr'{processing_path}\{file}'
    mv(source_path,target_path)

    # loading the dataset in dataframe and loading in a csv on output path 
    df_parent = pd.read_csv(target_path, sep=',',skiprows=20)
    final_dataframe=df_parent.dropna(subset=['Description','Balance'],how='all')
    
    # downloading the final dataframe and creating an output file in output directory
    timestamp=f'{datetime.now().strftime("%Y%m%d%H%M%S")}'
    output_file_name=f"output_{file.split('.')[0]}_{timestamp}.csv"
    output_file_path=fr'{output_path}\{output_file_name}'
    final_dataframe.to_csv(output_file_path, index=False)
    print(f"output file has been saved to {output_file_path}")

    ## Archive the file 
    archive_file_name=f"{file.split('.')[0]}_{timestamp}.csv"
    source_path=fr'{processing_path}\{file}'
    target_path=fr'{archive_path}\{archive_file_name}'
    mv(source_path,target_path)



    

