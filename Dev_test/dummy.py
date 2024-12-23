
import pandas as pd

target_path=r'C:\Users\Metac\Downloads\Python-Learning\Python-Learning\Dev_test\data\SEP-2022.csv'
sub=pd.read_csv(target_path, sep=',',index_col=None)
sub_df=sub.iloc[4:19,:2].copy()
sub_df_transpose=sub_df.T
sub_df_transpose.reset_index(drop=True, inplace=True)
sub_df_chg_headrs=sub_df_transpose.copy()
sub_df_chg_headrs.columns = sub_df_chg_headrs.iloc[0]
sub_df_chg_headrs = sub_df_chg_headrs[1:]  
#sub_df_chg_headrs.to_csv('sub_df_T.csv',index=True)
 
 # print(sub_df_transpose)

sub_df_address=sub.iloc[:4,:2].copy()
sub_df_address=sub_df_address.T
sub_df_address.columns=sub_df_address.iloc[0]
sub_df_address=sub_df_address[1:]
sub_df_address['Address'] = sub_df_address.agg(' '.join, axis=1)
sub_df_address=sub_df_address['Address']
# sub_df_address.to_csv('sub_df_address.csv',index=False)

result_outer = pd.merge(sub_df_chg_headrs, sub_df_address, how='cross')

result_outer.to_csv('sub_df_final.csv',index=False)