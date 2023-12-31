"""
[큰 수의 법칙]
다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다.
단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 이 법칙의 특징
N : 배열의 크기
M : 숫자가 더해지는 총 횟수 
K : 특정 인덱스가 최대 연속해서 더할 수 있는 수
"""

# 단순하게 푸는 답안 예시
# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력 받은 수들 정렬하기
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번쨰로 큰 수

result = 0 # 초기값

while True:
    for i in range(k): # 가장 큰 수를 K번 더하기
        if m == 0: # m이 0이라면 반복문 탈출
            break
        result += first # 제일 큰 수를 result에 더하기
        m -=1 # 더할 때마다 1씩 빼기
    if m == 0: # m이 0이라면 반복문 탈출
        break
    result += second # 두 번쨰로 큰 수 더하기
    m -= 1 # 더할 때마다 1씩 빼기

print(result)

"""
위 풀이는 M이 10,000 이하이므로 이 방식으로도 문제를 해결할 수 있지만, M의 크기가 100억 이상처럼 커진다면
시간 초과 판정을 받을 것이다. 아래와 같은 수학적 지식으로 더욱 효율적인 알고리즘을 짤 수 있다.
가장 먼저 반복되는 수열에 대해서 파악해야한다.

가장 큰 수 와 두 번쨰로 큰 수가 더해질 때는 특정한 수열 형태로 일정하게 반복해서 더해지는 특징이 있다.
예를 들어 N(배열의 크기)이 5이고, M(숫자가 더해지는 총 횟수)이 8이고, K(특정 인덱스가 최대 연속해서 더할 수 있는 수)가 3이고 
입력값이 2 4 5 4 6이라고 생각해보자.

(6+6+6+5) (6+6+6+5) 정답은 46이 될 것이다.
위의 예시를 통해 반복되는 수열에 길이는 (k+1) 즉, 4가 된다.
따라서 M을 (K+1)로 나눈 몫이 수열이 반복되는 횟수가 된다.
다시 여기에 K를 곱해주면 가장 큰 수가 등작하는 횟수가 나온다.

이떄 M이 (K+1)이 나누어떨어지지 않는 경우도 고려해야 한다. 그럴 떄는 M을 (K+1)로 나눈 나머지만큼 가장 큰 수가 추가로 더해지므로
이를 고려해주어야 한다. 즉 가장 큰 수가 더해지는 횟수는 아래와 같다.

int(M / (K + 1)) * K + M % (K + 1)
"""

# 답안 예시
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번쨰로 큰 수 더하기

print(result)
