#중복빼고 N개의 정수 오름차순 정렬하기
#10867
import sys
input = sys.stdin.readline

N = int(input())
num = set(map(int, input().split()))
num_sorted = sorted(num) #그냥 num만 print해도 오름차순되던데 백준엔 틀렸다고뜸

sys.stdout.write(' '.join(map(str, num_sorted)))
