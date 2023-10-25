"""
[1이 될 떄까지]
어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다. 
단, 두 번쨰 연산은 N이 K로 나누어떨어질 떄만 선택할 수 있다.
1. N에서 1을 뺀다.
2. N을 K로 나눈다.

N과 K가 주어질 떄 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 
최소 횟수를 구하는 프로그램을 작성해라.
"""

# 단순하게 푸는 답안 예시
n, k = map(int, input().split())
result = 0

# N이 K 이상이라면 K로 계속 나누기
while n >= k:
    # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 뺴기
    while n % k != 0:
        n -= 1
        result += 1
    # k로 나누기
    n //= k
    result += 1

# 마지막으로 남은 수에 대하여 1씩 뺴기
while n > 1:
    n -= 1
    result += 1

print(result)

# N이 K의 배수가 되도록 효율적으로 한 번에 빼는 방식
n, k = map(int, input().split())
result = 0

while True:
    # (N == K로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # N이 K보다 작을 떄(더 이상 나눌 수 없을 떄) 반복문 탈출
    if n < k:
        break
    # k로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += -1
print(result)



