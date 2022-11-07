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