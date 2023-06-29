'''
Lever 무조건 지나야 한다는 조건 추가 못 함 

1 x 1 크기의 칸들로 이루어진 직사각형 격자 형태의 미로에서 탈출하려고 합니다. 각 칸은 통로 또는 벽으로 구성되어 있으며, 벽으로 된 칸은 지나갈 수 없고 통로로 된 칸으로만 이동할 수 있습니다. 통로들 중 한 칸에는 미로를 빠져나가는 문이 있는데, 이 문은 레버를 당겨서만 열 수 있습니다. 레버 또한 통로들 중 한 칸에 있습니다. 따라서, 출발 지점에서 먼저 레버가 있는 칸으로 이동하여 레버를 당긴 후 미로를 빠져나가는 문이 있는 칸으로 이동하면 됩니다. 이때 아직 레버를 당기지 않았더라도 출구가 있는 칸을 지나갈 수 있습니다. 미로에서 한 칸을 이동하는데 1초가 걸린다고 할 때, 최대한 빠르게 미로를 빠져나가는데 걸리는 시간을 구하려 합니다.

미로를 나타낸 문자열 배열 maps가 매개변수로 주어질 때, 미로를 탈출하는데 필요한 최소 시간을 return 하는 solution 함수를 완성해주세요. 만약, 탈출할 수 없다면 -1을 return 해주세요.
'''

class Stack:
    def __init__(self):
        self.top = []
    def isEmpty(self):
        return len(self.top) == 0
    def size(self):
        return len(self.top)
    def clear(self):
        self.top = []
    def push(self, item):
        self.top.append(item)
    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
    def peek(self):
        if not self.isEmpty():
            return self.top[-1]

def solution(maps):
    count = -1
    lever_pushed = False
    finished = False
    maps_list = []
    for i, mapp in enumerate(maps):
        map_list = []
        for j, mark in enumerate(mapp):
            if mark == 'S':
                start = (j, i)   
                print(start)
            map_list.append(mark)
        maps_list.append(map_list)

    def isValidPos(x, y):
        if 0 <= y < len(maps_list) and 0 <= x < len(maps_list[y]):
            if maps_list[y][x] in ['O','E']:
                return True
            elif maps_list[y][x] == 'L':
                lever_pushed = True
                return True
        return False
    stack = Stack()
    stack.push(start)
    while not stack.isEmpty():
        here = stack.pop()
        print(here, end="->")
        if here is None:
            break
        (x, y) = here
        if (maps_list[y][x] == 'E') & (lever_pushed == True):
            stack.push((x , y))
            finished = True
            count += 1
            break
        else:
            if maps_list[y][x] == 'X':
                return True
            else:
                if maps_list[y][x] == "L":
                    lever_pushed = True
                maps_list[y][x] = '.'
                if isValidPos(x, y - 1):
                    stack.push((x, y - 1))
                    count += 1
                if isValidPos(x, y + 1):
                    stack.push((x, y + 1))
                    count += 1
                if isValidPos(x - 1, y):
                    stack.push((x - 1, y))
                    count += 1
                if isValidPos(x + 1, y):
                    stack.push((x + 1, y))
                    count += 1
        
    if finished:
        return count
    else:
        return -1