number = int(input())
genre = {
    'Horror': 0, 'Romance': 0, 'Comedy': 0, 
    'History': 0, 'Adventure': 0, 'Action': 0}


for i in range(0,number):
    inputs = input().split(' ')
    name= inputs[0]
    fav_genre = inputs[1:]
    for i in fav_genre:
        genre[i] = genre[i]+1

#4
# hossein Horror Romance Comedy
# mohsen Horror Action Comedy
# mina Adventure Action History
# sajjad Romance History Action
       
outputs = genre.items() 
# print(outputs,"\n")  
# dict_items([('Horror', 2), ('Romance', 2), ('Comedy', 2), ('History', 2), ('Adventure', 1), ('Action', 3)]) 

outputs = sorted(outputs, key=lambda item: (item[1],-(ord(item[0][0])-100)), reverse=True)
# print(outputs)    
# [('Action', 3), ('Comedy', 2), ('Horror', 2), ('History', 2), ('Romance', 2), ('Adventure', 1)]    

for i in outputs:
    print("%s : %i"% (i[0],i[1])) 
# Action : 3
# Comedy : 2
# Horror : 2
# History : 2
# Romance : 2
# Adventure : 1
