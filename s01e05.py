string = input().replace(",","").split(" ")

# remove spaces
for index,i in enumerate(string):
    string[index] = string[index].strip(" ")
    
counter = 1
tmp = []
for i in string:
    if counter != 1:
        if string[counter-2] != "." and string[counter-2][-1] != ".":
            if i[0].isupper():
                tmp.append((counter,i))
    counter += 1
    
# print(tmp)
# [(2, 'Persian'), (3, 'League'), (15, 'Iran.'), (17, 'Persian'), (18, 'League')]   
    
if tmp == []:
    print(None)
else:
    for i in tmp:
        print(f"{i[0]}:{i[1].strip('.')}")
        
# 2:Persian
# 3:League
# 15:Iran
# 17:Persian
# 18:League         
        