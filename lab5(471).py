numbers = list(map(int, input().split()))

result = [number for number in numbers if number != 0]
result.sort(reverse=True)

print(result)
