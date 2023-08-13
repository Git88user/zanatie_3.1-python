list = ["Informatika", "obsherazvivaushiy", "predmet", "dlya", "nastoyashego", "programmista"]
vowels = "eyuioa"
newwords = []
count = 0
i = 0

while i < len(list):
    for char in list[i].lower():
        if char in vowels:
            count += 1
    if count >= 3:
        newwords.append(list[i])
    count = 0
    i += 1

print(newwords)