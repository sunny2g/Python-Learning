import pandas as pd 



def Convert_csv():
    pass


# Read Excel data from data/may file 
df = pd.read_excel(r'C:\Users\Metac\Downloads\Python-Learning\Python-Learning\Data_Cleaning\data\May-2022.xlsx',engine='openpyxl')
# print(df)

# column_names=df.columns
# 
# for i in column_names:
#     print(f"Columns Names - {i}")

# Row1= df.iloc[0,1]
# print(f"Printing row 1 - {Row1}")
# 
# print(column_names)

col1=df.columns[0]
col1_val=df.columns[1]
# print(f" Name - {col1} , Value - {col1_val}")
col2=df.iloc[0,0]
col2_val=df.iloc[0:4,1 ]
# print(f" Name - {col2} , Value - {col2_val} ")
col3=df.iloc[4,0]
col3_val=df.iloc[4,1]

col4=df.iloc[5,0]
col4_val=df.iloc[5,1]

col5=df.iloc[6,0]
col5_val=df.iloc[6,1]

col6=df.iloc[7,0]
col6_val=df.iloc[7,1]

col7=df.iloc[8,0]
col7_val=df.iloc[8,1] 

col8=df.iloc[9,0]
col8_val=df.iloc[9,1]

col9=df.iloc[10,0]
col9_val=df.iloc[10,1]

col10=df.iloc[11,0]
col10_val=df.iloc[11,1]

col11=df.iloc[12,0]
col11_val=df.iloc[12,1]

col12=df.iloc[13,0] 
col12_val=df.iloc[13,1] 

col13=df.iloc[14,0]
col13_val=df.iloc[14,1]

col14=df.iloc[15,0]
col14_val=df.iloc[15,1]

col15=df.iloc[16,0]
col15_val=df.iloc[16,1]

col16=df.iloc[17,0]
col16_val=df.iloc[17,1]

col17=df.iloc[18,0]
col17_val=df.iloc[18,1]


# print(df.iloc[19,0],df.iloc[19,1] )

num_rows = len(df)

for i in range(20,num_rows):
    col18=df.iloc[19,0]
    col18_val=df.iloc[i,0]
    # print(col18_val)

for i in range(20,num_rows):
    col19=df.iloc[19,1]
    col19_val=df.iloc[i,1]
    # print(col19_val)

for i in range(20,num_rows):
    col20=df.iloc[19,2]
    # print(col20)
    col20_val=df.iloc[i,2]
    # print(col20_val)

for i in range(20,num_rows):
    col21=df.iloc[19,3]
    #print(col21)
    col21_val=df.iloc[i,3]
    print(col21_val)


for i in range(20,num_rows):
    col21=df.iloc[19,3]
    #print(col21)
    col21_val=df.iloc[i,3]
    print(col21_val)