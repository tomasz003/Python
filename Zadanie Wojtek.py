#Ustalamy n. Czy istnieje maksymalne ograniczenie na x=(m+1)*(m/2+n) takie, żeby m+n|x?

def is_divisible(a,b):
    if a%b==0:
        return 1
    else: 
        return 0 


n=1

for n in range (2, 101):
    m=1
    print(f"{n}, {n**2}, {((n-1)**2-1)}")
    print()
    while(m<1000000):
        if (((m+1)*(m/2+n))%(m+n))==0:
            print(f"{m}: {round((m+1)*(m/2+n))}")
        else: 
            pass
        
        m+=1
    print()

print("slay")