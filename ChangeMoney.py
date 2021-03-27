# 500 100 50 10
N = int(input())
num = 0 # 거슬러 줘야 할 돈 갯수

coin_types=[500 ,100 ,50 ,10]
for coin in coin_types:
    num = num + N//coin # // 는 몫(무조건 정수), /는 나누기(소수점으로 뜬다)
    N = N%coin # 가장 큰 숫자부터 나눠주고 난 후 남은 돈
print(num)