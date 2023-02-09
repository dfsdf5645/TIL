import sys
sys.stdin = open('sample_input.txt', encoding='utf-8')

def make_lps(pattern):
    # 중계리스트
    lps = [0] * len(pattern)

    # lps의 각 인덱스에 이전 패턴정보 담기위한 인덱스
    lps_idx = 0
    for i in range(1, len(pattern)):
        # 이전번 글자와 지금 조사하는 글자가 같다면
        if pattern[lps_idx] == pattern[i]:
            lps[i] = lps_idx + 1
            lps_idx += 1
        else:
            #다를 때는 0으로 초기화시켜서 패턴의 0번째와 다시비교
            lps_idx = 0
            if pattern[i] == pattern[lps_idx]:
                lps[i] = lps_idx + 1
                lps_idx += 1
    return lps

def KMP(pattern, target):
    lps = make_lps(pattern)
    #조사 시작은 brute force 방법과 동일하게 시작
    p_idx = 0
    t_idx = 0
    count = 0
    while t_idx < len(target):
        if pattern[p_idx] == target[t_idx]:
            t_idx += 1
            p_idx += 1
        else:
            if p_idx == 0:
                t_idx += 1
            else:
                p_idx = lps[p_idx - 1]
        if p_idx == len(pattern):
            count += 1
            p_idx = 0
    return count

T = int(input())
for tc in range(1, T+1):
    target, pattern = input().split()  # 전체문자와 찾아야하는 문자 따로 받기
    # KMP 함수는 전체문자에서 찾아야하는 문자가 몇번나왔는지 카운트값 리턴
    ans = KMP(pattern, target) + (len(target) - (len(pattern) * KMP(pattern, target)))
    # 답은 카운트값 + ( 전체문자 길이 - ((찾는문자열 길이)*카운트값) )
    print(f'#{tc} {ans}')