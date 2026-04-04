# List of Dictionaries

cars = [
  {"brand":"Toyota","model":"Corolla","year":"2022"},
  {"brand":"Honda","model":"Civic","year":"2021"},
  {"brand":"Ford","model":"Mustang","year":"2023"},
  {"brand":"BMW","model":"3 Series","year":"2020"},
  {"brand":"Mercedes-Benz","model":"C-Class","year":"2022"},
  {"brand":"Audi","model":"A4","year":"2021"},
  {"brand":"Nissan","model":"Altima","year":"2023"},
  {"brand":"Hyundai","model":"Elantra","year":"2022"},
  {"brand":"Chevrolet","model":"Camaro","year":"2021"},
  {"brand":"Kia","model":"Sportage","year":"2023"}
]

cars[0]["year"] = 2099
print("=-=-=-=-= Hot Cars =-=-=-=-=")
for car in cars:
    print("__________________")
    print("brand:",car["brand"])
    print("model:",car["model"])
    print("year:",car["year"],"\n")