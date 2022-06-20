def normalizer(datas):
    normalized_data = []
    print(datas)
    for data in datas:
        print(data)
        normalized_data.append(normalize('NFKC', data).rstrip())
    return normalized_data


def simplify(text):
    import unicodedata
    text = unicodedata.normalize('NFD', str(text)).encode(
        'ascii', 'ignore').decode("utf-8")
    return text


def text_cleaner(txt):
    no_whitespace_txt = []
    stripped_txt = []
    for elem in txt:
        cleaned_txt = simplify(elem)
        no_whitespace_txt.append(" ".join(cleaned_txt.split()))
        stripped_txt.append(elem.split(": "))
    print(stripped_txt)
    return stripped_txt


# def text_cleaner(txt):
#     txt = txt.split("\n")
#     no_whitespace_txt = []
#     for elem in txt:
#         no_whitespace_txt.append(" ".join(elem.split()))
#     stripped_txt = []
#     for elem in no_whitespace_txt:
#         stripped_txt.append(elem.split(": "))
#     return stripped_txt
