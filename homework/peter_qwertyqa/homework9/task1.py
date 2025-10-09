from datetime import datetime

date = "Jan 15, 2023 - 12:05:33"

# %b - сокращенное название месяца
dt_formatted = datetime.strptime(date, "%b %d, %Y - %H:%M:%S")
print(dt_formatted.strftime("%B"))
print(dt_formatted.strftime("%d.%m.%Y, %H:%M"))
