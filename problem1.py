
j, k = 3, 5 
n = 1000
sum = 0
#count all multiple of threes
for i in range(0,n,3):
    sum += i
#count all multiple of five that are not also multiple of 3     
for i in range(0,n,5):
    if i % 15:
        sum += i
        
print(sum)

