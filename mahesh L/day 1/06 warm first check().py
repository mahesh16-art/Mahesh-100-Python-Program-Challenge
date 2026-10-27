import sys

sys.path.insert(0, ",,/src")
from course_tools import check, check_output

answer = 6 * 8          
check(answer, 42)

check(answer, 42, hint="Multiplication is written with *, so six times seven is 6 * 7.")
