first = [int(x) for x in input().replace(',', ' ').split()]
second = set(int(x) for x in input().replace(',', ' ').split())

result = []
seen = set()

for number in first:
    if number in second and number not in seen:
        result.append(number)
        seen.add(number)

print(*result)
