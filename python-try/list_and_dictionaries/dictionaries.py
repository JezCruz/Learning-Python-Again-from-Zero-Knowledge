# Lists and Dictionaries - dictionaries

cars = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2022
}

print(cars["brand"])

cars["year"] = 2026
cars["color"] = "Cyan"


for key, value in cars.items():
    print(key, ":",value)