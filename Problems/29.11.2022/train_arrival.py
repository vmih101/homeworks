import datetime

h1m1 = input('Input the departure time (format HH:MM, e.g. 13:30)... ')
h2m2 = [int(i) for i in (input('Input the time on the way (format HH:MM, e.g. 13:30)... ').split(':'))] 

departure = datetime.datetime.strptime(h1m1, '%H:%M')
way = datetime.timedelta(hours=h2m2[0], minutes=h2m2[1]) #timedelta arguments may be integers or floats !
arrival = departure + way

print(f"Arrival time is {arrival.strftime('%H:%M')}")
