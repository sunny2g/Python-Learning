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


incoming_path=fr'{os.getcwd()}\data\incoming'
processing_path=fr'{os.getcwd()}\data\processing'

file_pattern = os.path.join(f'{incoming_path}', '*')
all_incoming_files=glob.glob(file_pattern)
file_names = [os.path.basename(file) for file in all_incoming_files]
for file in file_names:
    if file.split('.',-1)[-1] == 'xls':
        xls_file = fr'{incoming_path}\{file}'
        old_name=fr'{incoming_path}\{file}'
        new_name=file.split('.')[0]
        new_name=f'{new_name}.txt'
        # This will rename all xls files to txt files 
        os.rename(fr'{incoming_path}\{file}', fr'{incoming_path}\{new_name}')
        # Now move the file to processing/ path from incoming
        source_path=fr'{incoming_path}\{new_name}'
        target_path=fr'{processing_path}\{new_name}'
        shutil.move(source_path,target_path)

        # step 3
        df_parent = pd.read_csv(target_path, delim_whitespace=True, header=None,skiprows=21)
        print(df_parent)

        
# print(file_names)

file_path=os.getcwd()
pattern = os.path.join(f'{file_path}\data', '*.xlsx')
files = glob.glob(pattern)

for file in files:
    # Read Excel data from data/may file 
    df = pd.read_excel(rf'{file}',engine='openpyxl')
    new_header=df.iloc[19]
    new_dataframe=df.iloc[20:].copy()
    new_dataframe.columns=new_header
    new_dataframe.reset_index(drop=True,inplace=True)
    final_dataframe=new_dataframe.dropna(subset=['Description','Balance'],how='all')
    # final_dataframe.to_csv('output_file.csv', index=False)
    



