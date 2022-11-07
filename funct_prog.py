def multipy_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

print(multipy_by2([8,6,7]))

def square_item(item):
    return item*item

#MAP
print(list(map(square_item, [4,5,6])))

#Filter
def check_odd(item):
    return item % 2 != 0

print(list(filter(check_odd, [2,3,4,5,6])))