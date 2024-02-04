l= [10,11,12,20,25,18,19,78,15,21,45,78,12,44,11,20]
def list(l,function):
    new_list=[]
    for i in l:
        if function(i):
            new_list.append(i)
    return new_list
even_list = list(l, lambda i:  i % 2 ==0)
odd_list = list (l, lambda i:  i % 2 !=0)

print(l)
print(even_list)
print(odd_list)