import sys

sys.stdin = open('file.in', 'r')
sys.stdout = open('file.out', 'w')

positions = str(input())
positions = positions.replace(',', '')
positions = [int(x) for x in positions.split()]
floor = 0
for i in positions:
    floor += i
print(floor)
