string="Abhsihek"

for i in range(len(string)-1,-1,-1):
    print(string[i],end=" ")
print("\n")

print("\n")
print("Reversing a string")
string="Chatterjee"
stre=""
for i in range(len(string)-1,-1,-1):
    stre=stre+string[i]+" "
print(stre)

numbers = [123,121]
for i in range(len(numbers)):
    numbers[i] = int(str(numbers[i])[::-1])
print(numbers)

print("\n")
print("Reversing a list and checking the palindrome")
list=[513,121,123,141]
list_1=[]
for i in list:
    list_1.append(i)
for j in range(len(list_1)):
    list_1[j]=int(str(list_1[j])[-1::-1])
print("The REVERSED LIST IS -->",list_1)

for t in range(len(list)):
    if list[t]==list_1[t]:
        print("Palindrome-->",list[t])
    else:
        print("Not palindrome -->",list[t])

print("\n")
print("Manually reversing a Number")
num=122
sum=0
while(num>0):
    a=num%10
    sum=sum*10+a
    num=num//10
print("The Number is reversed-->",sum)