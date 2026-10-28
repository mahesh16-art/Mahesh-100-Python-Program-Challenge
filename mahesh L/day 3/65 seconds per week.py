import sys

sys.path.insert(0, ",,/src")
from course_tools import check, check_output

print("setup complete ✔ ")

seconds_per_week = 7*24*60*60
check(seconds_per_week, 604800)
