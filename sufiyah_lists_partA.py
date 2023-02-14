#Sufiyah Sajan
#Lists

#Part A

def prime_numbers(N):
    prime_numbers = []
    numbers =['P' for i in range(0, N+1)]
    numbers[0]='N'
    numbers[1]='N'
    start_index = 2
    while start_index < N:
        while not numbers[start_index] == 'P':
            start_index += 1
        prime_numbers.append(start_index)
        num = 2
        while (start_index * num) < N:
            numbers[start_index * num] = 'N'
            num += 1
        start_index += 1
    print("All prime numbers from 0 to", N)
 
    cnt = 0
    for i in prime_numbers:
        print(i, end = '\t')
        cnt = (cnt+1)%10
        if cnt == 0:
            print()

num = int(input("Enter a number range: "))

prime_numbers(num)

