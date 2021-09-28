class Flight():
    def __init__(self, capactity): # creates a new flight
        self.capacity = capactity
        self.passengers = [] # create an list of empty passengers

    def add_passenger(self, name): # method that will work on an individual object
        if not self.open_seats(): #if no open seats
            return False
        self.passengers.append(name) # add name to passenger list by using append
        return True

    def open_seats(self): # tells us how many open seats there are
        return self.capacity - len(self.passengers) # len will get you the num of passengers b/c its a sequence of things


flight = Flight(3) # 3 people on this flight, and we'll have an empty list of passengers

people = ["Harry", "Ron", "Hermoine", "Ginny"]
for person in people: #loop over all of those people
    success = flight.add_passenger(person) #calling add_passenger
    if success:
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}")


# to optimize:
"""
people = ["Harry", "Ron", "Hermoine", "Ginny"]
for person in people: #loop over all of those people
    if flight.add_passenger(person): #calling add_passenger
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}")
"""