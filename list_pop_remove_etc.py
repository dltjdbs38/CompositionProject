from collections import deque
# collections 모듈의 deque 클래스 사용 (double ended queue)
# 양 쪽에서 뺄 수 있음.
a=[1,2,3]

a.insert(1, "apple") # 두 번째에 apple 추가
print(a) # [1, 'apple', 2, 3]

a.append('boat') # 무조건 맨 뒤에 boat 추가
print(a) # [1, 'apple', 2, 3, boat]

a.pop(3) # 네 번쨰(0 1 2 3) 원소 제거
print(a) # [1, 'apple', 2, boat]

a.pop() # 맨 마지막 원소 제거
print(a)

############pop은 시간복잡도 O(n)이므로 한칸씩 미뤄주고 제거해서
# 효율이 좋지 않음.
# 그러니 양 쪽에서 빼고 넣을 수 있는 deque 사용
b= deque([1,2,3])

b.append('apple')
print(b)
print(b[0]) # indexing이 된다

b.popleft() # pop은 맨 뒤에서 뺴는데 얘는 맨 앞을 뺄 수 있다.
print(b)

b.appendleft('line') # append인데 맨 앞에 넣을 수 있음
# insert보다 빠른 연산
print(b)



