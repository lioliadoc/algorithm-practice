# Add your clarifying questions here

def skyline(building_list):
    build_set = set()
    for i in range(len(building_list)):
        if building_list[i] > 0:
            build_set.add(building_list[i])
    return sorted(list(build_set))

assert skyline([-1, 1, 3, 7, 7, 3]) == [1,3,7]
print("tests passed")