import os
fformat = str(input('Enter format type (e.g. .jpeg): '))

for filename in os.listdir("."):
        if filename.startswith('formatCov.py') is False: #converts all the file except for the Python File
            os.rename(filename,filename+fformat)
    
    
