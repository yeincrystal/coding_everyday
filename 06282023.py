'''
고객의 약관 동의를 얻어서 수집된 1~n번으로 분류되는 개인정보 n개가 있습니다. 약관 종류는 여러 가지 있으며 각 약관마다 개인정보 보관 유효기간이 정해져 있습니다. 당신은 각 개인정보가 어떤 약관으로 수집됐는지 알고 있습니다. 수집된 개인정보는 유효기간 전까지만 보관 가능하며, 유효기간이 지났다면 반드시 파기해야 합니다.

예를 들어, A라는 약관의 유효기간이 12 달이고, 2021년 1월 5일에 수집된 개인정보가 A약관으로 수집되었다면 해당 개인정보는 2022년 1월 4일까지 보관 가능하며 2022년 1월 5일부터 파기해야 할 개인정보입니다.
당신은 오늘 날짜로 파기해야 할 개인정보 번호들을 구하려 합니다.

모든 달은 28일까지 있다고 가정합니다.
'''
def solution(today, terms, privacies):
    term_list = [(term.split()[0], int(term.split()[1])) for term in terms]
    today_year, today_month, today_day = map(int, today.split('.'))
    today_date = f"{today_year}.{today_month}.{today_day}"    
    answer = []
    for i, privacy in enumerate(privacies):
        date, term_type = privacy.split()
        year, month, day = map(int, date.split('.'))
        term_tmp = next(term[1] for term in term_list if term[0] == term_type)
        year += (month + term_tmp) // 12
        month = (month + term_tmp) % 12
        if day == 1:
            day = 28
        else:
            day -= 1
        termination_dt = f"{year}.{month}.{day}"
        if termination_dt < today_date:
            answer.append(i + 1)
    return answer
