import sys

sys.stdin = open('coast.in', 'r')
sys.stdout = open('coast.out', 'w')

values = [str(x) for x in input().split()]
# North = 0, East = 1, South = 2, West = 3
# Left = 4, Right = 5
facing = 1
x = 0
y = 0


def moveindirection(d, a, x, y):
    if d == 'N':
        y += a
    elif d == 'S':
        y -= a
    elif d == 'E':
        x += a
    else:
        x -= a
    return x, y


def turn(d, a, direction):
    if d == 'L':
        a = int(a / 90)
        direction -= a
        direction = int(direction % 4)
    elif d == 'R':
        a = int(a / 90)
        direction += a
        direction = int(direction % 4)
    return direction


for i in values:
    direction = i[0]
    amount = int(i[1:])
    if direction == 'E' or direction == 'S' or direction == 'N' or direction == 'W':
        x, y = moveindirection(direction, amount, x, y)
    elif direction == 'L' or direction == 'R':
        facing = turn(direction, amount, facing)
    else:
        facingdirection = 'E'
        if facing == 0:
            facingdirection = 'N'
        elif facing == 1:
            facingdirection = 'E'
        elif facing == 2:
            facingdirection = 'S'
        else:
            facingdirection = 'W'
        x, y = moveindirection(facingdirection, amount, x, y)
print(x, y)
