# dynamically modifying sys.path would have been required
# if we hadn't created a package
# import sys
# sys.path.insert(1, "./subpackage1")


from ..subpackage1 import file3

print("This is file5.py")
