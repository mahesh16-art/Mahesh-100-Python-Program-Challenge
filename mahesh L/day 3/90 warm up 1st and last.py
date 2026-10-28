import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output


word = "Python"

first = "p"
last = "n"
first_three = "pyt"
last_three =  "hon"
check(first, "P")
check(last, "n")
check(first_three, "Pyt")
check(last_three, "hon")
                                     
