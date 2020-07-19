ls=list(map(int,input().split(" ")))
n=ls[0]
ls=ls[1:]
par_lst=[]
for i in ls:
    dig=[int(x) for x in str(i)]
    # print(dig)
    pre_ele =(max(dig)*11)+(min(dig)*7)
    par_lst.append(pre_ele)
    dig.clear()
# print(par_lst)
t_lst=[]
for i in par_lst:
    ln=str(i)
    if len(str(i))==3:
        t_lst.append(int(ln[1:]))
    else:
        t_lst.append(int(ln))
# print(t_lst)
pair=[]
even_list=t_lst[::2]
odd_list=t_lst[1::2]
even_list_first=[]
odd_list_first=[]
# print(even_list)
# print(odd_list)
for i in even_list:
    even_list_first.append(int(str(i)[0]))
for i in odd_list:
    odd_list_first.append(int(str(i)[0]))

for i in even_list_first:
    count=even_list_first.count(i)
    if count>=2:
        pair.append(i)
        even_list_first.remove(i)
        count=0
for i in odd_list_first:
    count=odd_list_first.count(i)
    if count>=2:
        pair.append(i)
        odd_list_first.remove(i)
        count=0

print(len(pair))