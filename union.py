import sys

file_name = sys.argv[1]
file_input = open(file_name)
input_list = []

for line in file_input: 
    line = line.strip()    
    words = line.split() 
    if words:
         input_list.append(words)

sorted_list = sorted(input_list,key = lambda x:x[1])

#Reducer

current_word = None
current_number = 0
word = None

for key,value in sorted_list:

    word = key  
    number = value

    if(current_number != number):
        print('%s \t %s' % (word,number))  

    current_number = number
    current_word = word

