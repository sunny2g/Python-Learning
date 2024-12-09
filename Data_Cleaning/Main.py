import pandas as pd 
import glob
import os
file_path=os.getcwd()
pattern = os.path.join(f'{file_path}\data', '*.xlsx')
files = glob.glob(pattern)
print(files)

for file in files:
    # Read Excel data from data/may file 
    df = pd.read_excel(rf'{file}',engine='openpyxl')
    new_header=df.iloc[19]
    new_dataframe=df.iloc[20:].copy()
    new_dataframe.columns=new_header
    new_dataframe.reset_index(drop=True,inplace=True)
    final_dataframe=new_dataframe.dropna(subset=['Description','Balance'],how='all')
    final_dataframe.to_csv('output_file.csv', index=False)  
