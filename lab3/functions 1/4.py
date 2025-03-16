
def is_prime(n):
    if n <= 1:
        return False  
    
    for i in range(2, int( (n ** 0.5) + 1) ): #  округляет вниз 
        if n % i == 0:
            return False  
    
    return True

def filter_prime(num):
    return list(filter(is_prime, num))

numbers = input ( "enter list numbers: " )
numbers_list = list(map (int, numbers.split () ))

prime_n = filter_prime( numbers_list )
print ( f"prime numbers: {prime_n}" )

    