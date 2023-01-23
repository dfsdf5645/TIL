# A.    입력 예시 
# ['eat','tea','tan','ate','nat','bat']

# B.    출력 예시 
# [ ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat'] ] 

# 1.  문자열 배열을 받아 애너그램 단위로 그룹핑하는 
# 함수 group_anagrams을 작성하여라.

def group_anagrams(list_name):
    new = []
    mix = []
    for idx in range(len(list_name)):
        a = sorted(list_name[idx])
        b = ''.join(a)
        mix.append(b)
        # mix = ['aet', 'aet', 'ant', 'aet', 'ant', 'abt']
    for i in range(len(mix)):
        empty = []
        for j in range(len(mix)):
            if mix[i] == mix[j]:
                empty.append(list_name[j]) #mix쓰면 [['aet','aet','aet'],['ant','ant'],['bat']] 이렇게 나옴
                #반드시 원본값인 list_name에서 같은 인덱스를 뽑아와야 정답 나옴
                #그 안에서 정렬만 바뀌고 인덱스 위치는 같으니까
            else:
                continue
        if empty not in new:
            new.append(empty)
    return new

print(group_anagrams(['eat','tea','tan','ate','nat','bat']))