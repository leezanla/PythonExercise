"""判断两个集合是否相等"""
s = {1, 2, 3, 4}
s1 = {4, 3, 2, 1}
print(s == s1)  # True


"""一个集合是否是另一个集合的子集"""
s2 = {10, 20, 30, 40, 50}
s3 = {10, 20, 30, 40}
s4 = {10, 20, 1000}
print(s3.issubset(s2))  # True
print(s4.issubset(s3))  # False

"""一个集合是否是另一个集合的超集"""
print(s2.issuperset(s3))  # True
print(s3.issuperset(s4))  # False

"""两个集合是否含有交集"""
print(s3.isdisjoint(s4))  # False 有交集为False
s5 = {300, 400, 500}
print(s3.isdisjoint(s5))  # True 没有交集为True































