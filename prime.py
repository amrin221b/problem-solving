def primeN(num):
    for i in range(2,num):
        if num%i == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
            
primeN(int(input('check the number is prime or not: ')))