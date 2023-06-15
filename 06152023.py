import numpy as np
def solution(targets):
    answer = 0
    #끝점을 기준으로 정렬하기
    targets.sort(key=lambda x: x[1])
    temp = 0
    #끝점이 가장 앞에 있는 구간을 먼저 선택하기
    for i in targets:
        #맨 처음에는 띄어넘기
        #두 번 째부터는 앞에 구간의 끝점보다 시점이 앞서면 통과 (추가 선 생성하지 않아도 됨)
        if i[0]<temp:
            continue
        #앞의 끝점보다 시작점이 뒤에 있으면 새로운 선 필요 (카운트 추가하기)
        else:
            answer+=1
            #맨 처음에는 첫 구간의 끝점 선택
            #그 다음부터는 시점이 이전 끝점 이후인 점의 끝점으로 업데이트
            temp = i[1]

    return answer
    print(targets)

