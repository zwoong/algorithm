"""
선택 정렬은 알고리즘 문제 풀이에 사용하기에는 느린 편이다. 그렇다면 다른 접근 방법에 대해서 생각해보자.
'데이터를 하나씩 확인하며, 각 데이터를 적절한 위치에 삽입하면 어떨까?'
삽입 정렬은 선택 정렬처럼 동작 원리를 직관적으로 이해하기 쉬운 알고리즘이다.

물론 삽입 정렬은 선택 정렬에 비해 구현 난이도가 높은 편이지만 선택 정렬에 비해 실행 시간 측면에서 더 효율적인 알고리즘으로
잘 알려져 있다. 특히 삽입 정렬은 필요할 때만 위치를 바꾸므로 '데이터가 거의 정렬 되어 있을 떄' 훨씬 효율적이다.
선택 정렬은 현재 데이터의 상관없이 무조건 모든 원소를 비교하고 위치를 바꾸는 반면 삽입 정렬은 그렇지 않다.

삽입 정렬은 특정한 데이터를 적절한 위치에 '삽입'한다는 의미에서 삽입 정렬이라고 부른다.
더불어 삽입 정렬은 특정한 데이터가 적절한 위치에 들어가기 이전에, 그 앞까지의 데이터는 이미 정렬되어 있다고 가정한다.
정렬되어 있는 데이터 리스트에서 적절한 위치를 찾은 뒤에, 그 위치에 삽입된다는 점이 특징이다.
"""

# 삽입 정렬 소스코드
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1,len(array)):
    #  인덱스 i부터 1까지 감소하며 반복하는 문법
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]: # 한 칸씩 왼쪽으로 이동
            array[j], array[j - 1] = array [j - 1], array[j]
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break;        

print(array)
    
"""
삽입 정렬의 시간 복잡도는 O(N제곱)인데, 선택 정렬과 마찬가지로 반복문이 2번 중첩되어 사용되었다.
실제로 수행 시간을 테스트해보면 앞서 다루었던 선택 정렬과 흡사한 시간이 소요되는 것을 알 수 있다.
여기서 꼭 기억할 내용은 삽입 정렬은 현재 리스트의 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 동작한다는 점이다.

최선의 경우 O(N)의 시간 복잡도를 가진다. 바로 다음에 배울 퀵 정렬 알고리즘과 비교했을 떄, 보통은 삽입 정렬이
비효율적이나 정렬이 거의 되어 있는 상황에서는 퀵 정렬 알고리즘보다 더 강력하다.
"""