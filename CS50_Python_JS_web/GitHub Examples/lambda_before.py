people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Raveclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

# def a function that tells the sort function how to do the sorting
def f(person): # need to tell sort function how to sort these people
    return person["house"] # sort by persons name/house

people.sort(key = f) # sort the people by running this function

print(people)