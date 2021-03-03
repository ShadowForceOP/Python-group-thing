import sys

sys.stdin = open('citystate.in', 'r')
sys.stdout = open('citystate.out', 'w')

n = int(input())
cities = {}
answer = 0
for thing in range(n):
    a, b = map(str, input().split())
    try:
        cities[a[:2]].append(b)
    except KeyError:
        cities[a[:2]] = []
        cities[a[:2]].append(b)


for i in cities:
    for j in cities[i]:
        exists = False
        state = j
        try:
            x = cities[state]
            if i != state:
                exists = True
        except KeyError:
            continue
        if exists:
            for g in x:
                if g == i:
                    answer += 1


print(int(answer / 2))
