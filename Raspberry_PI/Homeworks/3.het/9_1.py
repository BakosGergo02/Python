def factorization(n):
    if n < 2:
        return "n !>1"
    
    factors = []
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            factors.append(i)
            
    if factors:
        return factors
    else:
        return f"{n} egy prím szám"

number = 20
print(factorization(number))
