

import re


n = 2
inp = [
    ".*\+",
    ".*+"
]

for r in inp:
    try:
        re.compile(r)  # use compile to validate pattern
        print "True"
    except re.error:  # raise re.error for all regex errors
        print "False"

