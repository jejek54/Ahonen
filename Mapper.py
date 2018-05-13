import sys

file_name = sys.argv[1]
file_input = open(file_name)

for line in file_input: 
    line = line.strip()    
    words = line.split()
    
    for word in words:        
        print '%s\t%s' % (word, 1)


