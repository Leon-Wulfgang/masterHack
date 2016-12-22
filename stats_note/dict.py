"""
Dictionary of Statistics terms.
"""
from pprint import pprint

d = {
    'mean': "aka Average, sum/count, mean(2,4,5)== %s " % ((2 + 4 + 5) / 3),
    'median': "element in middle after sort, median(2,2,4,5) == (2+4)/2 == 3 ",
    'mode': "most popular element, mode(2,2,4,5) == 2, mode(1,1,2,2,3) == (1,2) multimodal ",
    'precision': "number of significant digits, precision(123.45) == precision(0.012345) == 5 ",
    'scale': "number of digits to the right of decimal point, scale(0.0123) == 4 ",
}

pprint(d)