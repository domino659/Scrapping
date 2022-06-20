from unicodedata import normalize


def normalizer(datas):
    normalized_data = []
    for data in datas:
        normalized_data.append(normalize('NFKC', data).rstrip())
    return normalized_data
