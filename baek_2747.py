# 재귀 또는 DP로 푼다
# 재귀는 f안에 f, DP는 DP table
n=int(input())
dp_list = [0 for i in range(n+1)] # 갯수가 n개인 list 만들기
dp_list[0]=0
dp_list[1]=1
 # DP 테이블의 값은 n번째 피보나치 수(sum)
for i in range(2, len(dp_list)):
    dp_list[i]=dp_list[i-1]+dp_list[i-2]
print(dp_list[n]) # refactor