import os
fformat = str(input('Enter format type (e.g. .jpeg): '))

for filename in os.listdir("."):
        if filename.startswith('smartrename.py') is False:
            os.rename(filename,filename+fformat)
    
    
