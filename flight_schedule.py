from pprint import pprint as p
airports = {"DCA": "Washington, D.C.",
            "IAD": "Dulles",
            "LHR": "London-Heathrow:",
            "SVO": "Moscow",
            "CDA": "Chicago-Midway:",
            "SBA": "Santa Barbara",
            "LAX": "Los Angeles",
            "JFK": "New York City",
            "MIA": "Miami",
            "AUM": "Austin, Minnesota"}

#Airline, Number, Destination, Gate, Time (Decimal Hours)
flights = [("Southwest", 145,  "DCA", 1, 6.00),
           ("United",    31,   "IAD", 1, 7.1),
           ("United",    302,  "LHR", 5, 6.5),
           ("Aeroflot",  34,   "SVO", 5, 9.00),
           ("Southwest", 146,  "CDA", 1, 9.60),
           ("United",    46,   "LAX", 5, 6.5),
           ("Southwest", 23,   "SBA", 6, 12.5),
           ("United",    2,    "LAX", 10, 12.5),
           ("Southwest", 59,   "LAX", 11, 14.5),
           ("American",  1,    "JFK", 12, 11.3),
           ("USAirways", 8,    "MIA", 20, 13.1),
           ("United",    2032, "MIA", 21, 15.1),
           ("SpamAir",   1,    "AUM", 42, 14.4)]


def flight_schedule(f):
    newFlights = []
    titles = ['Flight', 'Destination', 'Gate', 'Time']

    for x in range(0, len(f)):
        flights[x] = list(f[x]) #Changes the list of tuples to a list of lists
        for y in range(0, len(f[x])):
            if y == 1:
                f[x][y] = str(f[x][y]) #Changes the airline number to a string so the 0 and 1 element can be joined
            if y == 2:
                f[x][y] = airports[f[x][y]] #Converts the destination code to the destination name
        f[x][0:2] = [' '.join(f[x][0:2])] #Merges the 0 and 1 elements into a single element

    #Sorts the list of tuples by element
    newFlights = sorted(f, key=lambda x: x[3])  

    print('{:<20} {:<20} {:<20} {:<20}'.format(*titles)) #Unpacks list and spaces them by 20 units
    print 70*'-'
    for a in range(0, len(newFlights)):
        for line in [newFlights[a]]:
            print('{:<20} {:<20} {:<20} {:<20}'.format(*line)) #Unpacks list and spaces them by 20 units

flight_schedule(flights)