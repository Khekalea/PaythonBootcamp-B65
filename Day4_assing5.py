a=10
b=5

print("The first number is in Binary",bin(a))
print("The first number is",a)

print("The second number is in Binary",bin(b))
print("The Second number is",b)

result_and= a&b
print('This is "AND" operator in bin()',bin(result_and))
print('This is "AND" operator',result_and)

result_or= a|b
print('This is "OR" operator in bin()',bin(result_or))
print('This is "OR" operator',result_or)

result_xor= a^b
print('This is "XOR" operator in bin()',bin(result_xor))
print('This is "XOR" operator',result_xor)

result_not= ~a
print('This is "NOT" operator bin()',bin(result_not))
print('This is "NOT" operator ',result_not)

result_leftShift= a<<2
print('This is "LEFT SHIFT" operator bin()',bin(result_leftShift))
print('This is "LEFT SHIFT" operator ',result_leftShift)

result_rightShift= a>>2
print('This is "RIGHT SHIFT" operator bin()',bin(result_rightShift))
print('This is "RIGHT SHIFT" operator ',result_rightShift)




