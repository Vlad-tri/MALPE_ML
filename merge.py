import pandas as pd
df_list = []
filenames = ["",""]
for files in filenames:
    df_list.append(pd.read_csv(files))
    # df = pd.read_csv(files)
    # df.to_csv('dataset.csv', mode='a' ,index = False)
full_df = pd.concat(df_list)
full_df.to_csv('dataset.csv',index = False)
