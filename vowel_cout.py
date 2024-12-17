name = "gangadhar"
vowels = ('a','e','i','o','u')
count = 0
for i in range(0,len(name)):
    c = name[i]
    if(c in vowels):
        count = count+1

print(count)        
