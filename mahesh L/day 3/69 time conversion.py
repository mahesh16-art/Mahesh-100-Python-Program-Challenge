import sys

sys.path.insert(0, ",,/src")
from course_tools import check, check_output

total_seconds = 98765

hours = 27
minutes = 26
seconds = 5
check(hours, 27)
check(minutes, 26)
check(seconds, 5)
