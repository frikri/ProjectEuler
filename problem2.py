#limit
n = 4*10**6

sum = 2
#dynamic programming
fib = [1,2]
#starting with third fibonacci number 
i = 2 
#emulate do-while
while True:
    #fib[i%2] will be next fibonacci number
    fib[i%2] = fib[i%2] + fib[(i+1)%2]
    #break on threshold 
    if fib[i%2] >= n:
        break
    #add to sum if fibonacci number is even
    if fib[i%2]%2:
        sum += fib[i%2]
    i += 1

print(sum)