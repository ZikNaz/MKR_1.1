import random

def create_random_array(N):
    array = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(random.randint(1, 100))  
        array.append(row)
    return array

def calculate_average(row):
    return sum(row) / len(row)

N = 5  

array = create_random_array(N)

for row in array:
    print(row, "Середнє значення:", calculate_average(row))

sorted_array = sorted(array, key=calculate_average)

print("Відсортований масив:")
for row in sorted_array:
    print(row, "Середнє значення:", calculate_average(row))
