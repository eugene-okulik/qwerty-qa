import os
from datetime import datetime, timedelta

base_path = os.path.dirname(__file__)
parent = os.path.dirname(os.path.dirname(base_path))

file = os.path.join(parent, 'eugene_okulik', 'hw_13', 'data.txt')

dates = []

with open(file) as f:
    for line in f.readlines():
        # get datetime part of str line
        date = line[3:29]
        dates.append(datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f"))

# first datetime - add +7 days
print(dates[0] + timedelta(days=7))

# second datetime - print day of week
print(dates[1].strftime("%A"))

# third datetime - print how many day ago this date was
print((datetime.now() - dates[2]).days)
