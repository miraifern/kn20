import re
rnum=[]
string=input("enter a string of numbers and letters: ")
numar=re.findall(r'\d+', string)
string=re.sub(r"\d+", "", string, flags=re.UNICODE)
numar=[int(i) for i in numar]
print("letters: ", string, sep='')
print("numbers: ", numar, sep='')
def cap(string):
    string, result = string.title(), ""
    for word in string.split():
        result += word[:-1] + word[-1].upper() + " "
    return result[:-1]
print("\nline after change: ", cap(string), sep='')
print("max numbers",max(numar))
maxin=numar.index(max(numar))
i=0
for i in range(len(numar)):
    if i==maxin:
        continue
temp = numar[i] ** i
rnum.append(temp)
print("numbers after the change: ",rnum)