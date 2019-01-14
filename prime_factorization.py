"""
Prime Factorization - Have the user enter a number and find
all Prime Factors (if there are any) and display them.
"""

factors = lambda n: [x for x in range(1,n+1) if not n%x]
isprime = lambda n: len(factors(n)) == 2
primefactors = lambda n: list(filter(isprime,factors(n)))


def prime_fact(n):
    n = int(n)
    f = list(primefactors(n))
    return f"The prime factors of {n} are: {f}"

if __name__ == '__main__':
    
    print("Welcome to the Prime Factorizer.. Enter the numbers in the prompt or enter 'quit' to exit")

    while True:
        num = input(">>> ")
        if str(num).lower() == "quit" or str(num).lower() == "q":
            break
        else:
            print(prime_fact(num))