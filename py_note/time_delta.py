# https://www.hackerrank.com/challenges/python-time-delta
# in    string time
# out   time diff
#
# 1. datetime.strptime(date_string, format)  first convert string to datetime object with timezone info
#       strptime doesn't work on timezone for py2.x :
#           http://stackoverflow.com/questions/3305413/python-strptime-and-timezones
#       use from dateutil import parser instead [NOT A BUILD IN FUNCTION] for python 2.x

from datetime import datetime

n = 2
a = [
    [
        "Sun 10 May 2015 13:54:36 -0700",
        "Sun 10 May 2015 13:54:36 +0000"
    ],
    [
        "Sat 02 May 2015 19:54:36 +0530",
        "Fri 01 May 2015 13:54:36 +0000"
    ],
]
# %a weekday in short
# %d day of the month
# %B full name of month
# %Y full year
# %H 24 hr
# %M minute
# %S second
# %z UTC offset
my_format = "%a %d %B %Y %H:%M:%S %z"

for t1, t2 in a:
    t1_datetime_object = datetime.strptime(t1, my_format)
    t2_datetime_object = datetime.strptime(t2, my_format)
    print(abs(int((t1 - t2).total_seconds())))
