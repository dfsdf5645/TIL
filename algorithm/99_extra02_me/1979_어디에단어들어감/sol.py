#cnt가 끝나면(0인경우or끝idx인경우) 길이 비교
#arr[]==1인 경우 cnt+=1
#0이면 cnt==k인지 비교 후 cnt=0 초기화
#맨끝에 0넣어주면 경계확인가능
import sys
sys.stdin = open('input.txt')

def count(arr):
    ans = 0
    for lst in arr:
        cnt = 0
        for n in lst:
            if n == 1:      #단어 넣을 수 있는 공백
                cnt += 1
            else:
                if cnt == K:
                    ans += 1
                cnt = 0
    return ans

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(N+1)]

    #arr와 arr_t로 각 개수를 계산
    arr_t = list(map(list, zip(*arr)))
    ans = count(arr) + count(arr_t)
    print(f'#{tc} {ans}')
