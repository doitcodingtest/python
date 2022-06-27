n = input()
mylist = list(map(int, input().split()))
mymax = max(mylist)
sum = sum(mylist)
# 한 과목과 관련된 수식을 총합한 후 관련된 수식으로 변환해 로직이 간단해짐
print(sum*100/mymax/int(n))

