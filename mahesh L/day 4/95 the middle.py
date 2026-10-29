import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output

s = "abcdefghi"

middle =s[4]
outer_removed = (s[1:-1])
print(outer_removed)

check(middle, "e", hint="The middle index is len(s) // 2.")
check(outer_removed, "bcdefgh")
