def print_primes(n):
    for num in range(2, n + 1):  
        for i in range(2, num):
            if (num % i) == 0: 
                break
        else: 
            print(num)

n = int(input("Enter a number: "))
print_primes(n)
