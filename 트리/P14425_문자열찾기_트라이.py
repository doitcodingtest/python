from sys import stdin
input = stdin.readline

class Node(object):
    def __init__(self, isEnd):
        self.isEnd = isEnd
        self.childNode = {}


class Trie(object):
    def __init__(self):
        self.parent = Node(None)

    # 문자 삽입
    def insert(self, string):
        nowNode = self.parent
        temp_lenght = 0
        for char in string:
            # 자식 Node들 미 생성된 문자열이면 새로 생성
            if char not in nowNode.childNode:
                nowNode.childNode[char] = Node(char)
            # 자식 노드로 이동
            nowNode = nowNode.childNode[char]
            temp_lenght += 1
            if temp_lenght == len(string):
                nowNode.isEnd = True

    # 문자열이 존재하는지 탐색
    def search(self, string):
        nowNode = self.parent
        temp_lenght = 0
        for char in string:
            if char in nowNode.childNode:
                nowNode = nowNode.childNode[char]
                temp_lenght += 1
                if temp_lenght == len(string) and nowNode.isEnd == True:
                    return True
            else:
                return False
        return False


N, M = map(int, input().split())
myTrie = Trie()  # Trie생성

for _ in range(N):
    word = input().strip()
    myTrie.insert(word)  # 단어 삽입

result = 0
for _ in range(M):
    word = input().strip()
    if myTrie.search(word):  # 단어 찾기
        result += 1
print(result)
