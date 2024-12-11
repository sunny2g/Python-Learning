
import pandas as pd
# # Creating the original DataFrame
# data = {'col1': ['a1', 'a2', 'a3'],
#         'col2': ['b1', 'b2', 'b3']}
# df = pd.DataFrame(data)
# # Transpose the DataFrame and reset column names
# df_transposed = df.T  # Transpose the DataFrame
# # Add the column names as a row (header)
# df_transposed.columns = ['col1', 'col2', 'col3']
# # Print the final DataFrame
# print(df)


target_path=r'C:\Users\Metac\Downloads\Python-Learning\Python-Learning\Dev_test\data\SEP-2022.csv'
sub=pd.read_csv(target_path, sep=',')
sub_df=sub.iloc[4:19,:2].copy()
sub_df_transpose=sub_df.T

sub_df_transpose.columns=sub_df.iloc[0]
sub_df_transpose=sub_df_transpose.drop(0).reset_index(drop=True)



sub_df_transpose.to_csv('sub_df_T.csv',index=True) 

# df2 = pd.DataFrame([sub_df_transpose.iloc[1]] * 3, columns=sub_df_transpose.columns)
# 
# df2.to_csv('sub_df_T2.csv',index=True) 
# print(sub_df_transpose)
