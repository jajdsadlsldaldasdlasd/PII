# 5 task

N = int(input("Введите число, до которого будет вестись перебор"))
def sieve_of_eratosthenes(num):

    is_prime = [True] * (num + 1)
    is_prime[0] = is_prime[1] = False  

    
    for d in range(2, int(num**0.5) + 1):
        if is_prime[d]:
            for i in range(d * d, num + 1, d):
                is_prime[i] = False

   
    primes = [i for i in range(num + 1) if is_prime[i]]
    return primes
print(f"Все простые числа до вашего числа {N}:", *sieve_of_eratosthenes(N))
