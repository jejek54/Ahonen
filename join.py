import sys

file_name = sys.argv[1]
file_input = open(file_name)
input_list = []

for line in file_input: 
    line = line.strip()    
    words = line.split()
    if(words!= ""):
     if(words[0] == 'Orders'):
        del(words[0])
        input_list.append([words[1],words])
     else:
        del(words[0])
        input_list.append([words[0],words])
   

sorted_list = sorted(input_list,key=lambda x:x[0])

#Reducer
current_id = None
current_rest = 0
id_number = None

for key,value in reversed(sorted_list):    
    
    id_number = key  
    rest = value    

    if(id_number == current_id):
        print '%s\t%s%s' % (id_number, current_rest,rest)

    if(id_number != current_id):
        current_rest = rest
    current_id = id_number

