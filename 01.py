n = 600851475143

i = 2

while i * i <= n:
    while n % i == 0:
        n //=i
    i +=1

if n > 1:
    print(n)
else:
    print(i-1)