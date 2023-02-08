import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = input()          # 찾아야하는 문자열
    str2 = input()          # 찾을 문자열
    if str1 in str2:        # str1이 str2 안에 있다면
        ans = 1             # 1
    else:
        ans = 0
    print(f'#{tc} {ans}')

    # for i in range(len(str2)-len(str1)+1):
    #     if str1 == str2[i:i+len(str1)]:
    #         result = 1
    # print(f'#{tc} {result}')

