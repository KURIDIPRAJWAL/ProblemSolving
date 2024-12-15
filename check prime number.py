'''def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True'''

lower=int(input("enter lower number"))
upper=int(input("enter upper number"))
for num in range(lower,upper + 1):
    if num>1:
        for i in range(2,num):
            if num %i== 0:
                break
            else:
                print(num)

        

