# Add your clarifying questions here

def rotate_list(list, shift_by):
    for i in range(shift_by):
        popped_element = list.pop()
        list.insert(0, popped_element)
    return list

assert rotate_list([1, 2, 3, 4, 5], 3) == [3, 4, 5, 1, 2]
print("tests passed")

    