# 리스트 -> [1, 2, 3]
# 튜플 -> (1, 2, 3)
# 딕션너리 -> { 'a' : 1 }
a= [1, 2, 3]
print(f"리스트 형식 출력 해보기 : {a}")
b = tuple(a)
print(f"튜플 형식 출력 해보기 : {b}")
c = {'key' : 'value'}
print(f"딕션너리 형식 출력 해보기 : {c}")
d = set(a)
print(f"set(집합 : 중복불가) 형식 출력 해보기 : {d}")