import os, sys

# If 'python' is not recognised
print (os.path.dirname(sys.executable))

# If 'pip'/'auto-py-to-exe'/... is not recognised
print (os.path.dirname(sys.executable) + "\\Scripts")