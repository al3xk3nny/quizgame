# This is a dummy file to try sys.argv. It is not connected to "quiz.py". You still need to import sys into the "quiz.py" file.

import sys
print("This is the name of the script: ", sys.argv[0])
print("Number of arguments: ", len(sys.argv))
print("The arguments are: " , str(sys.argv))

# Run this and you will get;
# This is the name of the script:  tryargs.py
# Number of arguments:  1
# The arguments are:  ['tryargs.py']
# ...this is because the script always has at least 1 argument, the script name at position 0. 