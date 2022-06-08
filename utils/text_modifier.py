def simplify(text):
    import unicodedata
    try:
        text = unicode(text, 'utf-8')
    except NameError:
        pass
    text = unicodedata.normalize('NFD', text).encode(
        'ascii', 'ignore').decode("utf-8")
    return str(text)


def text_parser(txt):
    txt = txt.split("\n")
    no_whitespace_txt = []
    for elem in txt:
        no_whitespace_txt.append(" ".join(elem.split()))
    stripped_txt = []
    for elem in no_whitespace_txt:
        stripped_txt.append(elem.split(": "))
    return stripped_txt
