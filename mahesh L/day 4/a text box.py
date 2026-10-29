import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output

print("*" *10)
print("*" *1 + "        *" *1)
print("*" *1 + "  hi!  " " *" *1)
print("*" *1 + "        *" *1)
print("*" *10)
check_output("**********\n*        *\n*  Hi!   *\n*        *\n**********")
