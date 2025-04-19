num = [7,11,3,4]
for n in num:
    print(n)

print("-------------------------------")
num_2 = [7,11,3,4]
for index, n in enumerate(num_2):
    print(f"{index}:{n}")

print("-------------------------------")
num_3 = [[7,11,3,4], [2,6,5,9]]
for  n in num_3:
    print(n)

print("-------------------------------")
num_4 = [[7,11,3,4], 
        [2,6,5,9]]
for n in num_4:
    for j in n:
        print(j)

print("-------------------------------")
num_5 = [[7,11,3,4], 
        [2,6,5,9],
        [1,8,2,10]]

for row, n in enumerate(num_5):
    for column, j in enumerate(n):
        print(f"row{row}, column{column}:{j}")
