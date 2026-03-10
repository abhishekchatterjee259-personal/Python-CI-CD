string="kpit technologies"
s=string.split()

str=""
for i in s:
    str=str+i[0].upper()+i[1:-1]+i[-1].upper()+" "
print(str)
