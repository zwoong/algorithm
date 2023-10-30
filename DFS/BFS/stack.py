"""
Stack은 박스 쌓기에 비유할 수 있다. 흔히 박스는 아래에서부터 위로 차곡차곡 쌓는다.
그리고 아래에 있는 박스를 치우기 위해서는 위에 있는 박스를 먼저 내려야 한다. 이러한 구조를
선입후출(First In Last Out) 구조 또는 후입선출(Last In First Out)구조라고 한다.
"""

stack = []

# append : 리스트이 가장 뒤쪽에 데이터를 삽입
# pop : 리스트의 가장 뒤쪽에서 데이터를 삭제
# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # 최하단 원소부터 출력
print(stack[::-1]) # 최상단 원소부터 출력