import pandas as pd

class_1 = pd.DataFrame({"Name" : ["Sudha", "Priya", "Shree", "Shreya", "Sudha"], "Marks" : [10, 20, 30, 40, 50] })
class_2 = pd.DataFrame({"Name" : ["Sudha", "Ravi", "Raki", "Shree"], "Marks" : [30, 80, 10, 100]})
class_3 = pd.DataFrame({"Name" : ["Raja", "Ravi", "Priya", "Raja"], "Marks" : [10, 90, 60, 20]})
class_list = [class_1, class_2, class_3]

class_1['Status'] = 'Alive'
print(class_1)