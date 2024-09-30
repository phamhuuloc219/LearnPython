fruit_calories = {
    "apple": 130,
    "banana": 110,
    "avocado": 50,
    "cantaloupe": 50,
    "orange": 80,
    "grapefruit": 60,
    "pear": 100,
    "pineapple": 50,
    "lime": 20,
    "strawberries": 50,
    "watermelon": 80,
    "kiwifruit": 42,
    "peach": 60,
    "plums": 70,
    "nectarine": 62,
    "sweet cherries": 100,
    "blackberries": 62,
    "honeydew melon": 50,
    "papaya": 59,
    "tangerine": 50
}

def get_fruit_calories():
    fruit = input("Item: ").lower()
    
    if fruit in fruit_calories:
        print(f"Calories: {fruit_calories[fruit]}")
    else:
        print(f"The fruit type {fruit} is not listed or is invalid.")

if __name__ == "__main__":
    get_fruit_calories()
