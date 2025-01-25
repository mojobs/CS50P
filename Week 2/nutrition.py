fruits = {
    'apple': 130,
    'avocado': 50,
    'banana': 110,
    'sweet cherries': 100,
}

fruit = input("")
if fruit.lower() in fruits:
    print(f"Calories: {fruits[fruit.lower()]}")



