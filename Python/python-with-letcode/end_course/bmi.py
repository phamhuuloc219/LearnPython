def calculate_bmi(weight, height):
    return weight / (height ** 2)

def add_person(people, name, weight, height):
    people.append((name, weight, height))

def calculate_bmi_for_all(people):
    for person in people:
        name, weight, height = person
        bmi = calculate_bmi(weight, height)
        print(f"{name} - BMI: {bmi:.2f}")

def find_highest_lowest_bmi(people):
    if not people:
        return None, None

    highest = people[0]
    lowest = people[0]

    for person in people:
        name, weight, height = person
        bmi = calculate_bmi(weight, height)
        if bmi > calculate_bmi(highest[1], highest[2]):
            highest = person
        if bmi < calculate_bmi(lowest[1], lowest[2]):
            lowest = person

    return highest, lowest

def count_bmi_categories(people):
    categories = {"Gầy": 0, "Bình thường": 0, "Thừa cân": 0, "Béo phì": 0}

    for person in people:
        name, weight, height = person
        bmi = calculate_bmi(weight, height)
        if bmi < 18.5:
            categories["Gầy"] += 1
        elif 18.5 <= bmi < 24.9:
            categories["Bình thường"] += 1
        elif 25 <= bmi < 29.9:
            categories["Thừa cân"] += 1
        else:
            categories["Béo phì"] += 1

    return categories

people = []

while True:
    name = input("Nhập tên (hoặc 'exit' để kết thúc): ")
    if name.lower() == 'exit':
        break
    weight = float(input("Nhập cân nặng (kg): "))
    height = float(input("Nhập chiều cao (m): "))
    add_person(people, name, weight, height)
print("===========================================")
calculate_bmi_for_all(people)
print("===========================================")
highest, lowest = find_highest_lowest_bmi(people)
if highest and lowest:
    print(f"Người có BMI cao nhất: {highest[0]} - BMI: {calculate_bmi(highest[1], highest[2]):.2f}")
    print(f"Người có BMI thấp nhất: {lowest[0]} - BMI: {calculate_bmi(lowest[1], lowest[2]):.2f}")
print("===========================================")
categories_count = count_bmi_categories(people)
print("Số lượng người theo các loại BMI:")
for category, count in categories_count.items():
    print(f"{category}: {count}")
