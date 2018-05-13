import sys

file_name = sys.argv[1]
file_input = open(file_name)
input_list = []
stopwords = ['a','an','and','but','is','or','the','to','.',',']

for line in file_input: 
    line = line.strip()    
    words = line.split()
    for word in words:
        if(word not in stopwords):
            input_list.append([word,1])

input_list.sort()

#Reducer
current_word = None
current_count = 0
word = None

for key,value in input_list:    
    
    word = key  
    count = value
    count = int(count)
    
    if current_word == word:
        current_count += count
    else:
        if current_word:
           
            print '%s\t%s' % (current_word, current_count)
        current_count = count
        current_word = word

if current_word == word:
    print '%s\t%s' % (current_word, current_count)
