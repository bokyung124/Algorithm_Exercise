## 1. 문제

제 9 강에서 소개된 추상적 자료구조 LinkedList 는 dummy head node 를 가지는 연결 리스트입니다. 이 클래스의 아래와 같은 메서드들을, 강의 내용에 소개된 요구조건을 만족시키도록 구현하세요.

```python
popAfter()
popAt()
```

이 때, popAt() 메서드의 구현에서는 popAfter() 를 호출하여 이용하도록 합니다. (그렇게 하지 않을 수도 있지만, 여기에서는 popAfter() 의 이용에 의해서 코드 구현이 보다 쉬워지는 것을 확인하기 위함입니다.)

<br>

## 2. 풀이

```python
class Node:

    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = None
        self.head.next = self.tail


    def traverse(self):
        result = []
        curr = self.head
        while curr.next:
            curr = curr.next
            result.append(curr.data)
        return result


    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        i = 0
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr


    def insertAfter(self, prev, newNode):
        newNode.next = prev.next
        if prev.next is None:
            self.tail = newNode
        prev.next = newNode
        self.nodeCount += 1
        return True


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos != 1 and pos == self.nodeCount + 1:
            prev = self.tail
        else:
            prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)


    def popAfter(self, prev):
        curr = prev.next
        prev.next = curr.next
        if curr.next is None:
            self.tail = prev
        self.nodeCount -= 1
        return curr.data


    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        if pos == 1 and pos != self.nodeCount:
            self.head = pos.next
        else:
            prev = self.getAt(pos-1)
        return self.popAfter(prev)
            


def solution(x):
    return 0
```

<br>

## 3. 기억할 점

- 삽입, 삭제할 때 `self.nodeCount`도 변해야하는 것 잊지 말기!
- 따로 처리해주어야 하는 경우의 수 잘 세기!
    - 맨 앞 / 맨 뒤인 경우
    - 노드의 개수가 1개인 경우
    - 빈 노드인 경우 등등