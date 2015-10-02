'''
Takes a list of tuples and formats and arranges them in order of time first, then airline
'''
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
    #newFlights = []
    flightTime = []
    myorder = [1,2,3,0]
    titles = ['Flight', 'Destination', 'Gate', 'Time']

    for x in range(0, len(f)):
        flights[x] = list(f[x]) #Changes the list of tuples to a list of lists
        for y in range(0, len(f[x])):
            if y == 1:
                f[x][y] = str(f[x][y]) #Changes the airline number to a string so the 0 and 1 element can be joined
            if y == 2:
                f[x][y] = airports[f[x][y]] #Converts the destination code to the destination name
        f[x][0:2] = [' '.join(f[x][0:2])] #Merges the 0 and 1 elements into a single element

    #Manual sort by time
    for elem in flights:
        x = list(elem)
        x.insert(0,x[3])
        flightTime.append(x)
        
    flightTime2 = sorted(flightTime)

    #Sorts the list of tuples by element
    flightAirline = sorted(f, key=lambda x: x[0])


    print('{:<20} {:<20} {:<20} {:<20}'.format(*titles)) #Unpacks list and spaces them by 20 units
    print 70*'-'
    for a in range(0, len(flightTime2)):
        for line in [flightTime2[a]]:
            print('{:<20} {:<20} {:<20} {:<20}'.format(flightTime2[a][1], flightTime2[a][2], flightTime2[a][3], flightTime2[a][0])) #Rearranges list and spaces them by 20 units

    print('{:<20} {:<20} {:<20} {:<20}'.format(*titles)) #Unpacks list and spaces them by 20 units
    print 70*'-'
    for b in range(0, len(flightAirline)):
        for line in [flightAirline[b]]:
            print('{:<20} {:<20} {:<20} {:<20}'.format(*line)) #Unpacks list and spaces them by 20 units


flight_schedule(flights)