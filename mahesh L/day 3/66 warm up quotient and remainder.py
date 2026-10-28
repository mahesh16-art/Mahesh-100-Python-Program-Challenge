import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output


sweets = 17
children = 5
each = 6//2
left_over = 5%2
check(each,  3)
check(left_over, 2)
