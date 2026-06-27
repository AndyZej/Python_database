square = Square(11)

print(square.get_side())   # 11
print(square.side)         # 11
print(square.perimeter)    # 44

square.perimeter = 48

print(square.get_side())   # 12
print(square.side)         # 12
print(square.perimeter)    # 48