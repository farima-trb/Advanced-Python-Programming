import random

name_list= ["Hossein", "Mazyar", "Akbar", "Nnima", "Mahdi", "Farhad", "Mohammad", "Khashayar", "Milad", 
            "Mostafa", "Amin", "Saeid", "Pouya", "Pourya", "Reza", "Ali", "Behzad", "Soheil",
            "Behrouz", "Shahrouz", "Saman", "Mohsen"]

class Human():
    def __init__(self):
        self.names    = list(n for n in name_list)

    
class Footballist(Human):
    
    # Choosing team A or B randomly
    def select_team(self):
        # name_list=['Sam', 'Far', 'jad']
        team_list=[]
        
        for i in range(0,len(name_list)):
            team_list.append(random.randint(0,1))
        # [0, 1, 1]    
        
        # random.randint(0,1) --> 0 : team A , 1 : team B
            
        team_list=list(map(lambda x: "Team A" if x==0 else "Team B",team_list))
        # ['Team A', 'Team B', 'Team B']
        
        res=list(zip(name_list,team_list))
        # [('Sam', 'Team A'), ('Far', 'Team B'), ('jad', 'Team B')]
        
        return res    
        

for i in range(0,22):
    footballist_obj=Footballist()
    
print(footballist_obj.select_team())    
    



