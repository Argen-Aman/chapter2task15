print("let's count an inteval in seconds of two timestamps.")

h1 = int(input('The hour(s) of first timestamp: '))
m1 = int(input('The minute(s) of first timestamp: '))
s1 = int(input('The second(s) of first timestamp: '))
ts1 = 3600 * h1 + 60 * m1 + s1

h2 = int(input('The hour(s) of second timestamp: '))
m2 = int(input('The minute(s) of second timestamp: '))
s2 = int(input('The second(s) of second timestamp: '))
ts2 = 3600 * h2 + 60 * m2 + s2

print('The interval between given timestamps is ' + str(ts2 - ts1) + ' second(s).')
