
import pandas as pd 
import glob
import os
from datetime import datetime
import shutil

# Code Steps 
#
# 1. list out all the files in data incoming path and move 1 file into processing directory
# 1.1 check if file in xlxs format if not convert it . 
# 2. save the path in home_path variable and files names in file_name variable in processing directory
# 3. load the default data frame as df_parent variable from incoming file 
# 4. extract all the rows from file and create a copy in df_temp variable
# 5. create an output file and load the df_temp in output_files folder 
# 6. remove the file from processing directory
# 7. move the file from incoming path  to archive path with a timestamp 

## Optimization Steps 
# create small functions for each step and pull them from function file 
# Add try blocks to deal with errors 
# Add proper print messages for each step completion 
# extract remaining unformated data and add it in final dataframe 


incoming_path=fr'{os.getcwd()}\data\incoming'
processing_path=fr'{os.getcwd()}\data\processing'
archive_path=fr'{os.getcwd()}\data\archive'
output_path=fr'{os.getcwd()}\data\output'

file_pattern = os.path.join(f'{incoming_path}', '*.csv')
all_incoming_files=glob.glob(file_pattern)
file_names = [os.path.basename(file) for file in all_incoming_files]
for file in file_names:
    source_path=fr'{incoming_path}\{file}'
    target_path=fr'{processing_path}\{file}'
    shutil.move(source_path,target_path)

    # step 3 - loading the dataset in dataframe and loading in a csv on output path 
    df_parent = pd.read_csv(target_path, sep=',',skiprows=20)
    final_dataframe=df_parent.dropna(subset=['Description','Balance'],how='all')
    timestamp=f'{datetime.now().strftime("%Y%m%d%H%M%S")}'
    output_file_name=f"output_{file.split('.')[0]}_{timestamp}.csv"
    output_file_path=fr'{output_path}\{output_file_name}'
    final_dataframe.to_csv(output_file_path, index=False)

    ## Archive the file 
    archive_file_name=f"{file.split('.')[0]}_{timestamp}.csv"
    source_path=fr'{processing_path}\{file}'
    target_path=fr'{archive_path}\{archive_file_name}'
    shutil.move(source_path,target_path)



    

