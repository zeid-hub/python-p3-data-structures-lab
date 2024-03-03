spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    print([food['name'] for food in spicy_foods])
get_names(spicy_foods)


def get_spiciest_foods(spicy_foods):
    print([food for food in spicy_foods if food.get('heat_level', 0)>5])
get_spiciest_foods(spicy_foods)


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")
print_spicy_foods(spicy_foods)


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food.get('cuisine') == cuisine:
            print(food)
    return None
get_spicy_food_by_cuisine(spicy_foods, "American")

def print_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food['heat_level'] > 5]
    for food in spiciest_foods:
        heat_level = "🌶" * food['heat_level']
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")
print_spiciest_foods(spicy_foods)


def get_average_heat_level(spicy_foods):
    total_heat_level = sum(food['heat_level'] for food in spicy_foods)
    average_heat_level = total_heat_level / len(spicy_foods)
    print(average_heat_level)
get_average_heat_level(spicy_foods)


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    spicy_food ==  {'name': 'Spicy Tuna Salad', 'cuisine':'Japanese','heat_level':7}
    return spicy_food
created_tuna_salad = create_spicy_food(spicy_foods, spicy_foods)
print(created_tuna_salad)
print_spicy_foods(spicy_foods)
   