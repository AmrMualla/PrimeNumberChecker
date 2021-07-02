
#AmrMualla Basic PrimeNumber Checker
def prime_checker(number):
  answer = True
  for i in range(2, number, 1):
    if number %  i == 0:
      answer = False
  if answer:
    print("It's a prime number")
  else:
    print("It's not a prime number")
    
n = int(input("Check this number: "))
prime_checker(number=n)



