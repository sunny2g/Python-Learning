import pandas as pd 


target_path=r'C:\Users\Metac\Downloads\Python-Learning\Python-Learning\Dev_test\data\SEP-2022.csv'
sub=pd.read_csv(target_path, sep=',')
sub_df=sub.iloc[:19,:2].copy()

columns = sub_df.columns.tolist()
transposed_columns = [sub_df[col].to_frame().transpose() for col in columns]
new_df = pd.concat(transposed_columns, ignore_index=True)
temp_merged_df = pd.concat([new_df[0], new_df[1],new_df[2],new_df[3]], ignore_index=True)
temp_df=new_df.iloc[:,4:]
final_merged_df=pd.concat([temp_merged_df,temp_df],  ignore_index=True)
print([new_df[0], new_df[1],new_df[2],new_df[3]])
print(f"value - {new_df[1]}")

# final_merged_df.to_csv('sub_df.csv',index=False) 




   







"""
import json
from datetime import datetime

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}


# Specify the path where the file will be saved
current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
file_path = f"data/Sample_{current_datetime}.json"

# Open the file in write mode ('w') and use json.dump() to write data
with open(file_path, 'w') as file:
    json.dump(data, file, indent=4)  # 'indent=4' formats the JSON data for better readability

print(f"Data has been written to {file_path}")

"""






