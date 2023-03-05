"""Description
For a Railway Station, We are given arrival and departure timings of N trains in two arrays, let's call them Arrival and Departure.
We have to find the minimum number of platforms needed so that no train needs to wait for the railway station to have an empty platform.

"""

arrivals = [float(item) for item in input("Enter arrivals:").split()]
departures = [float(item) for item in input("Enter departures:").split()]

"""for every arrival , we can count an additional platform overlapping and remove a platform otherwise"""
combined_times = arrivals + departures
print(combined_times)
max_trains = []
sorted_time = sorted(combined_times)
print(sorted_time)
pf = 0
for each in sorted_time:
    if each in arrivals:
        pf = pf + 1
        max_trains.append(pf)
    if each in departures:
        pf = pf - 1
        max_trains.append(pf)

print(max(max_trains))


