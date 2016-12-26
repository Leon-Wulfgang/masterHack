# in date in format 08 05 2015
# out day in week upper case
import calendar

inp = "08 05 2015"
m, d, y = map(int, inp.split(' '))

print (calendar.day_name[calendar.weekday(y, m, d)]).upper()

