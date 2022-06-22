from unicodedata import normalize


def normalizer(datas):
    normalized_data = []
    for data in datas:
        normalized_data.append(normalize('NFKC', data).rstrip())
    return normalized_data


def array_to_nested_dict(arrays, number_index):
    var = arrays[0][1]
    dict = {}
    for array in arrays:
        dict[var[0] + "_" + array[0]
             ] = {number_index: j for i, j in enumerate(array[1:], 0)}
    # print(dict)
    return dict


def delete_useless_info(array):
    if "* Remarque" in array[-1][0]:
        array.pop()
    return array
