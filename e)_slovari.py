import csv

with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = {}
    for row in reader:
        name = row['Name']
        info = {'Gender': row['Gender'], 'Age': row['Age'], 'Salary':row['Salary']}
        data[name] = info

print(data)