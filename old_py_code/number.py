import sys
import cs50

numbers = [4,5,6,7,8,0]

if 0 in numbers:
    print("found")
    sys.exit(0)

print("Not Found")

sys.exit(1)