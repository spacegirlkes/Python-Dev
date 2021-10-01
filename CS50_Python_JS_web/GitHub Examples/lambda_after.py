people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Raveclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

# lambda person: person["name"] is a complete function. Takes a person as input and returns their name
people.sort(key = lambda person: person["name"]) # sort the people by running this function

print(people)