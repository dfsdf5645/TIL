def powerset(arr, K, result):
    global count
    if sum(result) > 10:
        return
    count += 1
    # 언제까지 부를거냐
    if K == len(arr):
        # 모든 result를 반환하진 않을거다
        if sum(result) == 10:
            print(result)
        return
    # K는 아무튼 증가하는데,
    # 그 K번째 쓴 경우
    powerset(arr, K+1, result + [arr[K]])
    # 그 K번째 안쓴 경우
    powerset(arr, K+1, result)


arr = list(range(1, 11))
count = 0

# 원본배열, 사용한 원소 수, 총합 리스트(사용할 원소 담을)
powerset(arr, 0, [])
print(count)