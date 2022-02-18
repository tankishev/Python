# Create a function named flights that receives a different number of arguments representing the information about the
# flights for a day:
# •	the destination of each flight
# •	the count of passengers that are boarding the plane
# •	a string "Finish"
# You need to take each argument and make a dictionary with the plane’s destination as a key and the passengers as a
# value of the corresponding key. If there are more than one flight to the same destination,
# you should count all the passengers that flew to the destination.
# You should modify the dictionary until the current argument is equal to "Finish".
# Note: Submit only the function in the judge system
# Input
# •	There will be no input, just parameters passed to your function
# Output
# •	The function should return the final dictionary


def flights(*args):
    retdict = {}
    flights_data = args[:args.index('Finish')]
    flights_destinations = [el for i, el in enumerate(flights_data) if i % 2 == 0]
    flights_passengers = [el for i, el in enumerate(flights_data) if i % 2 != 0]
    for cnt, flight in zip(flights_passengers, flights_destinations):
        if flight not in retdict:
            retdict[flight] = 0
        retdict[flight] += cnt
    return retdict
