def dict_init(clothes):
    cloth_dict = {}
    for cloth_name, cloth_type in clothes:
        if cloth_type in cloth_dict:
            cloth_dict[cloth_type].append(cloth_name)
        else:
            cloth_dict[cloth_type] = [cloth_name]
    return cloth_dict


def solution(clothes):
    clothes = dict_init(clothes)
    number = 1
    for value in clothes.values():
        number *= len(value) + 1
    return number - 1

