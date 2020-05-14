import pandas as pd
import numpy as np


household = pd.read_csv(r'/home/deras/Desktop/csv_parsing_new/Load_Profile.csv',index_col = False,dtype='unicode',delimiter = ',')
#print (household)
col_first = household.columns[0]
j = 0;
for i in range(1, household.shape[1]):
    col_i = household.columns[i]
    Path = '/home/deras/Desktop/csv_parsing_new/Load_Profile'+str(j)+'.csv'
    household.loc[:, [col_first, col_i]].to_csv((Path), index=False)
    j = 1 + j
