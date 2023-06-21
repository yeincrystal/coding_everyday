'''
문제 설명
지나다니는 길을 'O', 장애물을 'X'로 나타낸 직사각형 격자 모양의 공원에서 로봇 강아지가 산책을 하려합니다. 산책은 로봇 강아지에 미리 입력된 명령에 따라 진행하며, 명령은 다음과 같은 형식으로 주어집니다.

["방향 거리", "방향 거리" … ]
예를 들어 "E 5"는 로봇 강아지가 현재 위치에서 동쪽으로 5칸 이동했다는 의미입니다. 로봇 강아지는 명령을 수행하기 전에 다음 두 가지를 먼저 확인합니다.

주어진 방향으로 이동할 때 공원을 벗어나는지 확인합니다.
주어진 방향으로 이동 중 장애물을 만나는지 확인합니다.
위 두 가지중 어느 하나라도 해당된다면, 로봇 강아지는 해당 명령을 무시하고 다음 명령을 수행합니다.
공원의 가로 길이가 W, 세로 길이가 H라고 할 때, 공원의 좌측 상단의 좌표는 (0, 0), 우측 하단의 좌표는 (H - 1, W - 1) 입니다.
'''
def solution(park, routes):
    h = len(park)
    for p in park:
        w = len(p)
        break
    if (3<=len(park)<=50) and (1<=len(routes)<=50):
        #map을 dictionary 형태로 만들기
        e = []
        park_dict = {}
        for p in park:
            e += p 
        for h_e in range(h):
            for w_e in range(w):
                park_dict[e[0]] = [h_e, w_e]
                e = e[1:]
        #시작점 찾기
        for i, key in enumerate(park_dict):
            if key == 'S':
                start = park_dict[key]
                break
        #가로축으로 움직일 때 장애물 만나는 경우 실패 처리
        def test_w(here, route, direction, park_dict):
            test = [0,0]
            test[0] = here[0]
            test[1] = here[1]
            #오른쪽으로 움직일 때 (E)
            if direction == '+':
                for trial in range(int(route.split()[1])):
                    test[1] += 1
                    value = {i for i in park_dict if park_dict[i]==test}
                    if 'X' in value:
                        return 'Fail'
                        break  
            #왼쪽으로 움직일 때 (W)
            elif direction == '-':
                for trial in range(int(route.split()[1])):
                    test[0] -= 1
                    value = {i for i in park_dict if park_dict[i]==test}
                    if 'X' in value:
                        return 'Fail'
                        break    
        #세로축으로 움직일 때 장애물 만나는 경우 실패 처리
        def test_h(here, route, direction, park_dict):
            test = [0,0]
            test[1] = here[1]
            test[0] = here[0] 
            #아래쪽으로 움직일 때 (S)
            if direction == '+':
                for trial in range(int(route.split()[1])):
                    test[0] += 1
                    value = {i for i in park_dict if park_dict[i]==test}
                    if 'X' in value:
                        return 'Fail'
                        break  
            #위쪽으로 움직일 때 (N)
            elif direction == '-':
                for trial in range(int(route.split()[1])):
                    test[0] -= 1
                    value = {i for i in park_dict if park_dict[i]==test}
                    if 'X' in value:
                        return 'Fail'
                        break 

        here = start
        for route in routes:
            if route.split()[0] == 'E':
                #벽에 부딪히지 않고 장애물을 만나지 않으면 해당 경로로 이동
                if here[1] + int(route.split()[1]) <= w-1:
                    if test_w(here, route, '+' , park_dict) != 'Fail':
                        here[1] += int(route.split()[1])
                else:
                    pass

            elif route.split()[0] == 'W':
                if here[1] - int(route.split()[1]) >= 0:
                    if test_w(here, route, '-' , park_dict) != 'Fail':
                        here[1] -= int(route.split()[1])
                else:
                    pass

            elif route.split()[0] == 'S':
                if here[0] + int(route.split()[1]) <= h-1:
                    if test_h(here, route, '+' , park_dict) != 'Fail':
                        here[0] += int(route.split()[1])
                else:
                    pass

            elif route.split()[0] == 'N':
                if here[0] - int(route.split()[1])>= 0:
                    if test_h(here, route, '-' , park_dict) != 'Fail':
                        here[0] -= int(route.split()[1])
                else:
                    pass
        return here
    
    else:
        return None

    