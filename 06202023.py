'''
문제 설명
과제를 받은 루는 다음과 같은 순서대로 과제를 하려고 계획을 세웠습니다.

과제는 시작하기로 한 시각이 되면 시작합니다.
새로운 과제를 시작할 시각이 되었을 때, 기존에 진행 중이던 과제가 있다면 진행 중이던 과제를 멈추고 새로운 과제를 시작합니다.
진행중이던 과제를 끝냈을 때, 잠시 멈춘 과제가 있다면, 멈춰둔 과제를 이어서 진행합니다.
만약, 과제를 끝낸 시각에 새로 시작해야 되는 과제와 잠시 멈춰둔 과제가 모두 있다면, 새로 시작해야 하는 과제부터 진행합니다.
멈춰둔 과제가 여러 개일 경우, 가장 최근에 멈춘 과제부터 시작합니다.
과제 계획을 담은 이차원 문자열 배열 plans가 매개변수로 주어질 때, 과제를 끝낸 순서대로 이름을 배열에 담아 return 하는 solution 함수를 완성해주세요.
'''
#run time 줄여야 함..
def solution(plans):
    #plan을 [과목, 시작시간을 hours*60 + min 형태의 integer로, 소요시간]
    plans = map(lambda x: [x[0], int(x[1][:2])*60 + int(x[1][3:]), x[2]], plans) 
    plans = sorted(plans, key = lambda x: x[1])
    # print(plans)
    in_progress = []
    stopped = []
    finished = []
    for plan in plans:
        #수행 중인 과제가 없다면
        if len(in_progress) == 0: 
            in_progress.append([plan[0], plan[1], plan[2]])
        else:
            #만약 지금 하고 있는 과제의 끝보다 다음 과제의 시작 시간이 이르다면
            if int(in_progress[0][1]) + int(in_progress[0][2])  > int(plan[1]):
                stopped.append([in_progress[0][0], int(in_progress[0][1]) + int(in_progress[0][2]) - int(plan[1])])
                in_progress.pop()
                in_progress.append([plan[0], plan[1], plan[2]])
            #이르지 않다면 (순서대로 처리))
            else:
                left_time = int(plan[1]) - (int(in_progress[0][1]) + int(in_progress[0][2]))
                # print("left time",left_time)
                #순서대로 처리 하되
                finished.append(in_progress[0][0])
                in_progress.pop()
                in_progress.append([plan[0], plan[1], plan[2]])
                #중간에 비는 시간이 생긴다면
                if left_time > 0:
                    #남는 시간 동안에 중단되었던 과제 수행
                    tmp_sub = stopped.pop()
                    if left_time >= tmp_sub[1]:
                        finished.append(tmp_sub[0])
                        if left_time >= in_progress[0][2]:
                            finished.append(in_progress[0][0])
                            in_progress.pop()
                    else:
                        stopped.append([tmp_sub[0], tmp_sub[1] - left_time])
                    
    #마지막으로 진행 중이던 과제를 끝내고
    finished.append(in_progress[0][0])
    #밀려있던 과제 최근에 멈춘 순서로 끝내기
    while stopped:
        finished.append(stopped.pop()[0])
    return finished
 