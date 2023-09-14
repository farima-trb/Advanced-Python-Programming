from datetime import date

birthDate =input()
# 1995/02/03

birthDate = birthDate.split("/")
# print(birthDate)
#['1995', '02', '03']
birthDate_int=list(map(lambda x:int(x),birthDate))
# print(birthDate_int)
# [1995, 2, 3]

today = date.today()

if (birthDate_int[0]>today.year or birthDate_int[1]>12 or birthDate_int[1]<1 or birthDate_int[2]>31 or birthDate_int[1]<1):
    print("WRONG")

else:
    BD = date(birthDate_int[0],birthDate_int[1],birthDate_int[2])


    # age = today.year - BD.year -((today.month, today.day) < (BD.month, BD.day))

    age = today.year - BD.year
    print(age)
    # 24