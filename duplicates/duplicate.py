import pandas as pd

df_1 = pd.DataFrame({"Name" : ["Sudha", "Priya", "Shree", "Shreya"]})
df_2 = pd.DataFrame({"Name" : ["Sudha", "Ravi", "Raki", "Shree"]})
df = pd.concat([df_1, df_2], ignore_index=True)
print(df)
print(df[df.duplicated(['Name'], keep=False)])