from datetime import datetime
from time import strftime, strptime

h1m1 = input('Input the departure time (format HH:MM, e.g. 13:30)... ')
h2m2 = input('Input the arrival time (format HH:MM, e.g. 13:30)... ')

departure = datetime.strptime(h1m1, '%H:%M')
arrival = datetime.strptime(h2m2, '%H:%M')
way = datetime.strptime(str(arrival - departure), '%H:%M:%S')

print(f"The time on the way is {way.strftime('%H:%M')}")
