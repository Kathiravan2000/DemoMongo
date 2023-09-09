import random
import json

def generate_random_dishes():
    dishes = [
        "Spaghetti Carbonara", "Sushi Rolls", "Tacos", "Butter Chicken", "Peking Duck",
        "Croissant", "Tom Yum Soup", "Moussaka", "Caesar Salad", "Chow Mein",
        "Paella", "Bibimbap", "Pho", "Feijoada", "Kebab"
    ]
    
    num_dishes = random.randint(5, 15)
    restaurant_dishes = random.sample(dishes, num_dishes)
    
    return restaurant_dishes

def generate_random_restaurant():
    cuisines = [
        "Italian", "Japanese", "Mexican", "Indian", "Chinese",
        "French", "Thai", "Greek", "Mediterranean", "American",
        "Spanish", "Korean", "Vietnamese", "Brazilian", "Turkish"
    ]
    
    num_cuisines = random.randint(8, 15)
    restaurant_cuisines = random.sample(cuisines, num_cuisines)
    
    restaurant = {
        "name": f"Restaurant {random.randint(1, 1000)}",
        "address": f"{random.randint(1, 1000)} {random.choice(['Main St', 'Elm Ave', 'Oak Ln'])}",
        "city": f"City {random.randint(1, 10)}",
        "cuisines": restaurant_cuisines,
        "dishes": generate_random_dishes(),
        "rating": round(random.uniform(3.0, 5.0), 1)
    }
    
    return restaurant

restaurants = [generate_random_restaurant() for _ in range(500)]

with open('restaurants.json', 'w') as file:
    json.dump(restaurants, file, indent=4)

print("JSON file 'restaurants.json' created successfully.")
