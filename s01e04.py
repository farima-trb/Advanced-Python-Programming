number=int(input())
#4

f_list = []
m_list = []

for i in range(number):
    winner = input().split(".")
    winner[1] = winner[1].lower().capitalize()
    
    if winner[0] == "f":
        f_list.append(winner)
    elif winner[0] == "m":
        m_list.append(winner)

# m.hosSein.python
# f.miNa.C
# m.aHMad.C++
# f.Sara.java

# print("f_list:",f_list)  -->  f_list: [['f', 'Mina', 'C'], ['f', 'Sara', 'java']]
# print("m_list:",m_list)  -->  m_list: [['m', 'Hossein', 'python'], ['m', 'Ahmad', 'C++']]

        
# sort by alphabetical order of names        
f_list = sorted(f_list,key=lambda k : (k[1]))
m_list = sorted(m_list,key=lambda k : (k[1]))


# print("f_list:",f_list) -->  f_list: [['f', 'Mina', 'C'], ['f', 'Sara', 'java']]
# print("m_list:",m_list) -->  m_list: [['m', 'Ahmad', 'C++'], ['m', 'Hossein', 'python']]


res = [f_list,m_list]

# print(res)
# [[['f', 'Mina', 'C'], ['f', 'Sara', 'java']], [['m', 'Ahmad', 'C++'], ['m', 'Hossein', 'python']]]

# for gender in res:
#     for i in gender:
#         print(" ".join(i))

for i in range(0,len(res)):
    for j in range(0,len(res[0])):
        print(" ".join(res[i][j]))
# f Mina C
# f Sara java
# m Ahmad C++
# m Hossein python        


