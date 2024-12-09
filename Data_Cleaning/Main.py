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
    



