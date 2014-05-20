# Only a jerk would make this script into one single line!
# Doing this as a challenge

from sys import argv
from os.path import exists


open(argv[2],'w').write( open(argv[1]).read())

