"""
파이썬은 기본 정렬 라이브러리인 sorted() 함수를 제공한다. sorted()는 퀵 정렬과 동작 방식이 비슷한
병합 정렬을 기반으로 만들어졌는데, 병합 정렬은 일반적으로 퀵 정렬보다 느리지만 최악의 경우에도 시간 복잡도
O(NlogN)을 보장한다는 특징이 있다. 이러한 sorted() 함수는 리스트, 딕셔너리 자료형 등을 입력받아서
정렬된 결과를 출력한다. 
"""

# sorted 소스코드
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
result = sorted(array)
print(result)

# sort 소스코드
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
array.sort()
print(array)

# 정렬 라이브러리에서 key를 활용한 소스코드
array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting)
print(result)


