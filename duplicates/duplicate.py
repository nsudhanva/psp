import pandas as pd

class_1 = pd.DataFrame({"Name" : ["Sudha", "Priya", "Shree", "Shreya", "Sudha"], "Marks" : [10, 20, 30, 40, 50] })
class_2 = pd.DataFrame({"Name" : ["Sudha", "Ravi", "Raki", "Shree"], "Marks" : [30, 80, 10, 100]})
class_3 = pd.DataFrame({"Name" : ["Raja", "Ravi", "Priya", "Raja"], "Marks" : [10, 90, 60, 20]})
class_list = [class_1, class_2, class_3]

# print(class_1)
# print(class_2)
# df = pd.concat([class_1, class_2], axis=1)
# df = pd.append([df_1, df_2])
# print(df)

df_4 = pd.DataFrame()

# print(df_4.columns)

for df_1 in class_list:
    for df_2 in class_list:
        # print(df_1[df_1.duplicated(['Name'])], df_2[df_2.duplicated(['Name'])])
        df_3 = pd.concat([df_1, df_2], axis=1)
        df_4 = pd.concat([df_4, df_3])

# for df_a in df_list:
#     for df_b in df_list:
#         for i in range(len(df_a)):
#             for j in range(i, len(df_b)):
#                 if df_a['Name'][i] == df_b['Name'][j]:
#                     print(i, j)
#                     print(df_a['Marks'][i], df_b['Marks'][j])
#                     print(df_a['Name'][i], df_b['Name'][j])