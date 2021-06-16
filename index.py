n = 100000 #select an integer to find it's divisors
#n = int(input("Integer : ")) #//Or uncomment this line
divisors = []
for i in range(n,0, -1):
    if not n % i:
        divisors.append(i)
#divisors.reverse() #//Uncomment this line to see divisors in ascending order
print(divisors)
    
