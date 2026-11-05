numbers = list(map(int, input().split()))
n = int(input())

for number in numbers:
    if number < n:
        print(number, end=" ")
        
