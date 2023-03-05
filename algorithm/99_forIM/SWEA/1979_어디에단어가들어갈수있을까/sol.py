import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split()) #길이 K인 단어 몇개 들어가나
    pz = [input().replace(' ', '') for _ in range(N)]

    cnt = 0
    for n in pz:
        cnt += n.split('0').count('1'*K)

    pz2 = list(zip(*pz))
    for tp in pz2:
        s = ''
        for nn in tp:
            s += nn
        cnt += s.split('0').count('1'*K)
    print(f'#{tc} {cnt}')



