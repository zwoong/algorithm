"""
가로의 길이가 N, 세로의 길이가 2인 직사각형 형태의 얇은 바닥이 있다. 태일이는 이 얇은 바닥을 1 X 2의 덮개, 2 X 1의 덮개, 
2 X 2의 덮개를 이용해 채우고자 한다. 
이떄 바닥을 채우는 모든 경우의 수를 구하는 프로그램을 작성하시오.

[입력 조건]
- 첫째 줄에 N이 주어진다.
[출력 조건]
- 첫쨰 줄에 2 X N 크기의 바닥을 채우는 방법의 수를 796.796으로 나눈 나머지를 출력한다.
"""
# 답안 예시
n = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 1001

# 다이나믹 프로그래밍 진행(보텀업)
d[1] = 1
d[2] = 3
for i in range(3, n + 1):
    d[i] = (d[i - 1] + 2 * d[i - 2]) % 796796
  
# 계산된 결과 출력
print(d[n])
     