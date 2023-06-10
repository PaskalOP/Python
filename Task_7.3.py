# вернуть True, иначе вернуть False
#
# Примеры/Тесты:
#     same_by(lambda x: x % 2, [1, 2, 10, 12]) -> False
#     same_by(lambda x: x % 2, [0, 2, 10, 12]) -> True
#     same_by(len, ["qw", "er", "ty", "ui", "op", "as", "df", "gh"]) ->  True
#     same_by(len, ["qw", "er1", "ty", "ui", "op", "as", "df", "gh"]) -> False
#     same_by(max, ["qw", "er1", "ty", "ui", "op", "as", "df", "gh"]) -> False
#     same_by(max, ["qz", "zr1", "tz", "zi", "oz", "zs", "dz", "zh"]) -> True
#     same_by(lambda x: x[0], ["qz", "zr1", "tz", "zi", "oz", "zs", "dz", "zh"]) ->  False
#     same_by(lambda x: x[0], ["qz", "qr1", "qz", "qi", "qz", "qs", "qz", "qh"]) ->  True

def same_by(func, objects):
    if len(objects) == 0: return None
    for idx in range(1, len(objects)):
        if func(objects[idx]) !=  func(objects[idx-1]): return False
    return  True

print(same_by(len,["qw", "er", "ty", "ui", "op", "as", "df", "gh"]))
print(same_by(lambda x: x[0],["qw", "er", "ty", "ui", "op", "as", "df", "gh"]))
print (same_by(lambda x: x[0], ["qz", "qr1", "qz", "qi", "qz", "qs", "qz", "qh"]))