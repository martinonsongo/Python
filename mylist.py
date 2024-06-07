def listm():
    
my_list=[]
new=[10,20,30,40]
my_list.append(new)
print(my_list)
my_list.insert(2,15)
new_list=[50,60,70]
my_list.extend(new_list)
print(my_list)

del my_list[-1]
print(my_list)

index=my_list.index(50)
print(index)


my_list.sort()
print(my_list)