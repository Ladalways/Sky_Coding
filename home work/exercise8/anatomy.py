
import sys

argc = len(sys.argv)

if argc > 1:
    print("too many args")
else:
    where = "world"
    print("Hello", where)

print("goodbye from"+ sys.argv[0])
