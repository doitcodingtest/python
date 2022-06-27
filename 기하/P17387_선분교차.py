import sys
input = sys.stdin.readline
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

def CCW(x1, y1, x2, y2, x3, y3):
    temp = (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)
    if temp > 0:
        return 1
    elif temp < 0:
        return -1
    return 0

# 선분 겹침 여부 판별 함수
def isOverlab(x1, y1, x2, y2, x3, y3, x4, y4):
    if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(
            y1, y2):
        return True
    return False

def isCross(x1, y1, x2, y2, x3, y3, x4, y4):
    abc = CCW(x1, y1, x2, y2, x3, y3)
    abd = CCW(x1, y1, x2, y2, x4, y4)
    cda = CCW(x3, y3, x4, y4, x1, y1)
    cdb = CCW(x3, y3, x4, y4, x2, y2)
    if abc * abd == 0 and cda * cdb == 0:  # 선분이 일직선일 때
        return isOverlab(x1, y1, x2, y2, x3, y3, x4, y4)  # 겹치는 선분인지 판별
    elif abc * abd <= 0 and cda * cdb <= 0:  # 선분이 교차하는 경우
        return True
    return False

cross = isCross(x1, y1, x2, y2, x3, y3, x4, y4)
if cross:
    print(1)
else:
    print(0)
