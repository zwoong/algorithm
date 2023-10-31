"""
재귀 함수(Recursive Function) : 자기 자신을 다시 호출하는 함수를 의미한다.
컴퓨터 내부에서 재귀 함수의 수행은 스택 자료구조를 이용한다. 함수를 계속 호출했을 때 가장 마지막에 호출한
함수가 먼저 수행을 끝내야 그 앞의 함수 호출이 종료되기 떄문이다. 컴퓨터의 구조 측면에서 보자면 연속해서 호출되는 함수는
메인 메모리의 스택 공간에 적재되므로 재귀 함수는 스택 자료구조와 같다.

재귀 함수를 이용하는 대표적 예제로는 팩토리얼 문제가 있다. 팩토리얼 기호는 느낌표(!)를 사용하며 n!는
1 * 2 * 3 * ... * (n-1) * n을 의미한다.

팩토리얼을 반복적으로 구현한 방식과 재귀적으로 구현한 두 방식을 비교해보자.
"""

# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n + 1):
        result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

print('반복적으로 구현:', factorial_iterative(5))
print('재귀적으로 구현:', factorial_recursive(5))
