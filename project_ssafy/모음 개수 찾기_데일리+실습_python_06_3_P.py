# 1. 문자열을 전달 받아 해당 문자열의 모음 갯수를 반환하는 count_vowels
# 함수를 작성하시오.

def count_vowels(word):
    vowels = ['a','e','i','o','u'] #모음 리스트를 먼저 줌
    count = 0 #카운트 초기화
    for char in word: #주어진 단어의 알파벳 하나씩 순회하며
        if char in vowels: #모음 리스트안에 있을경우
            count += 1 #카운트 업
    return count

print(count_vowels('apple')) #=> 2
print(count_vowels('banana')) #=> 3