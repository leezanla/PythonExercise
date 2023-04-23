s = "hello, world"
print("1、", s.isidentifier())
# False,因为s字符串并不是由字母、数字、下划线组成，里面还有逗号

print("2、", "hello".isidentifier())  # True

print("3、", "\t".isspace())  # True

print("4、", "abc".isalpha())  # True 字符串是否合部由字符组成
print("5、", "张三".isalpha())  # True
print("6、", "张三1".isalpha())  # False

print("7、", "123".isdecimal())  # True
print("8、", "123四".isdecimal())  # False

print("9、", "123".isnumeric())  # True
print("10、", "123四".isnumeric())  # True, 也就是说 四 也是数字





























