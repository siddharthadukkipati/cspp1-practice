#define the gen_primes function here
def genPrimes():
    num = 2
    prime = True
    while True:
        if prime == True:
            yield num
        num = num + 1
        for i in range(2,num):
            if num % i == 0:
               prime = False
               break
        else:
            prime = True
def main():
	n = int(input())
primenum = genPrimes()
for i in range(n):
   print(primenum.__next__())
	
if __name__== "__main__":
	main()
