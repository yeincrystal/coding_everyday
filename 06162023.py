def solution(r1, r2):
    #지름 안에 있는 점을 포함하는 함수 만들기
    def total_dots(r):
        total_dots = (2*r -1)*(2*r -1) + 4
        return total_dots
    #경계선에 있는 점은 포함해 주기
    answer = total_dots(r2) - total_dots(r1) + 4
    return answer