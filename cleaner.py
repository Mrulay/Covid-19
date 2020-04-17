import pandas as pd

df1 = pd.read_csv(r"data\latest_stats.csv")
df2 = pd.read_csv(r"data\state_date_wise.csv")

df1['Location'].replace(["Nagaland#", "Telengana"], ["Nagaland", "Telangana"], inplace=True)
df2['Location'].replace(["Nagaland#", "Telengana"], ["Nagaland", "Telangana"], inplace=True)

df1.to_csv(r"data\latest_stats.csv")
df2.to_csv(r"data\state_date_wise.csv")
