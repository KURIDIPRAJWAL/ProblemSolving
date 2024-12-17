
def reverseNum(num):

    result = []
    while(num != 0):
        result.append(num%10)
        num =num//10
    for a in  result:
        print(a,end = "")

reverseNum(58225)     


