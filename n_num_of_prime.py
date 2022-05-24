# first n number of prime number

def Prime(n):  
    for i in range(2,n):  
        if(n%i==0):  
            return(0)  
    return(1)  
  
N=int(input("Enter N:"))  
i=2 
primes=[] 
while N!=0:  
    if(Prime(i)):  
        primes.append(i) 
        if(len(primes)==N): 
            break 
    i+=1 
print(f'First {N} Prime numbers are:')
print(*primes) 