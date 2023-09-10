# #عدد با بیشترین تعداد مقسوم علیه اول

numbers=[]
divisors=[]


# list of 10 numbers
for i in range(0,10):
    num=int(input())
    numbers.append(num)
    
# numbers= [6,25,13]    
 
# function of determining prime divisors number

def func(n):
    # First: get a number (n)
    # n=6
    
    # making the divisors list
    d=[]
    for i in range(1,n+1):
        if (n %  i ==0):
            d.append(i)
    # d=[1,2,3,6]
    
    # choosing the prime divisors 
    pd=[]       
    for j in range(0,len(d)):
        if d[j] > 1:
            # check for factors
            for i in range(2,d[j]):
                if (d[j] % i) == 0:
                    break
            else:
                pd.append(d[j])
    # pd=[2,3]
    
    # returning the number of prime divisors 
    return len(pd) 
    # 2         
                    
for i in range(0,len(numbers)):
    divisors.append(func(numbers[i]))
    
    
# list of [numbers,number of prime divisors]              
numbers_divisors=[]
numbers_divisors=[list(x) for x in zip(numbers,divisors)]    


# print("numbers:",numbers) 
# print("divisors:",divisors)  
# print("numbers_divisors:",numbers_divisors)
# 30
# 25
# 13
# numbers: [30, 25, 13]
# divisors: [3, 1, 1]
# numbers_divisors: [[30, 3], [25, 1], [13, 1]]
    

# finding [highest number,highest number of prime divisors] 

for i in range(0,len(numbers_divisors)):
	temp=numbers_divisors[i][0]
	numbers_divisors[i][0]=numbers_divisors[i][1]
	numbers_divisors[i][1]=temp
 
 
# print("numbers_divisors:",numbers_divisors)
# print("sorted:",numbers_divisors.sort())
# print("numbers_divisors:",numbers_divisors)
# print("final:",max(numbers_divisors))

k=max(numbers_divisors)
k.reverse()

print(k[0],k[1])