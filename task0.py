from random import randint 
vals = [randint(-100,100) for i in range(30)]
print(vals)
print("\nmax:",max(vals)) 
print("\nposition:",vals.index(max(vals))) 
for i in range(len(vals)-1):
    print(vals[i],vals[i+1])if vals[i]<0 and vals[i+1]<0 else None