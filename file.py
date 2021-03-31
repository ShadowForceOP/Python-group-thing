import sys

sys.stdin = open('file.in', 'r')
sys.stdout = open('file.out', 'w')

card, door = map(int, input().split())

subjectnumber = 7
loopsize = 0
power = 1
value = 1
# Finding the card's loop size
while value < card:
    value *= 7
    loopsize += 1
while value != card:
    value *= 7
    value = value % 20201227
    loopsize += 1
subjectnumber = door
value = 1
loopsize = 8
for i in range(loopsize):
    value *= subjectnumber
    value = value % 20201227
print(value)
