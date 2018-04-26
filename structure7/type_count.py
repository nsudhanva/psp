seq = ['LYS', 'LYS', 'SER']
temp_list = []
num = [0] * len(seq)

# print(num)
count = 1
index = 0

while index < len(seq) - 1:
    if seq[index] == seq[index + 1]:
        count = count + 1

    num[index] = count
    index = index + 1
    count = 1

    if index == len(seq) - 1:
        if seq[index] != seq[index - 1]:
            num[index] = count
    
print(num)
num = [0] * len(seq)

# print(num)
count = 1
index = 0

while index < len(seq) - 1:
    if seq[index] == seq[index + 1]:
        count = count + 1

    num[index] = count
    index = index + 1
    count = 1

    if index == len(seq) - 1:
        if seq[index] != seq[index - 1]:
            num[index] = count
    
print(num)