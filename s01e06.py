number = int(input())
#4

En = dict()
Fr = dict()
Gr = dict()

for i in range(0,number):
    word = input().split(" ")
    En[word[1]] = word[0]
    Fr[word[2]] = word[0]
    Gr[word[3]] = word[0]
    
# man I je ich
# kheili very très sehr
# alaghemand interested intéressé interessiert 
# barnamenevisi programming laprogrammation Programmierung

# print(En)
# {'I': 'man', 'very': 'kheili', 'interested': 'alaghemand', 'programming': 'barnamenevisi'}
# print(Fr)
# {'je': 'man', 'très': 'kheili', 'intéressé': 'alaghemand', 'laprogrammation': 'barnamenevisi'}
# print(Gr)
# {'ich': 'man', 'sehr': 'kheili', 'interessiert': 'alaghemand', 'Programmierung': 'barnamenevisi'}


sentence = input().split(" ")
# I am very interested in programming

# print(sentence)
# ['I', 'am', 'very', 'interested', 'in', 'programming']


for index,i in enumerate(sentence):
    if i in En:
        sentence[index] = En[i]
    elif i in Fr:
        sentence[index] = Fr[i]
    elif i in Gr:
        sentence[index] = Gr[i]

print(sentence)        
# ['man', 'am', 'kheili', 'alaghemand', 'in', 'barnamenevisi']

print(' '.join(sentence))
# man am kheili alaghemand in barnamenevisi