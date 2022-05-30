IDX = 0


def parse_tag(tmp_str, open_tags, close_tags):
    global IDX
    buf = ""
    IDX += 1
    while tmp_str[IDX] != "<":
        buf += tmp_str[IDX]
        IDX += 1

    attr = {}
    split_attr = buf.split(" ")
    attr["name"] = split_attr[-1][::-1]
    del split_attr[-1]
    for elem in split_attr:
        tmp_attr = elem.split("=")
        name_attr = tmp_attr[-1][::-1]
        del tmp_attr[-1]
        attr[name_attr] = "".join(tmp_attr)[::-1]

    if tmp_str[IDX - 1] == "/":
        attr["name"] = attr["name"][1:]
        close_tags.append(attr["name"])
        return True, attr
    open_tags.append(attr["name"])
    IDX += 1
    return False, attr


def parse_html(html_str: str, open_tag_callback, data_callback, close_tag_callback):
    global IDX
    IDX = 0
    res = []
    close_tags = []
    texts = []
    open_tags = []
    tmp_str = html_str[::-1]
    local_buf = ""
    while IDX != len(tmp_str):
        if tmp_str[IDX] == ">":
            texts.append(local_buf)
            local_buf = ""
            flag, tag = parse_tag(tmp_str, open_tags, close_tags)
            if not flag:
                open_tag_callback()
                if open_tags[-1] in close_tags:
                    tag_text = texts.pop()
                    tag["text"] = tag_text[::-1][:-1]
                    data_callback()
                    res.append(tag)
                    op_tag = open_tags.pop()
                    cl_tag = close_tags.pop()
                    if cl_tag != op_tag:
                        raise ValueError(f"Ожидался открывающий тэг {cl_tag}")
                    local_buf = texts.pop()
                else:
                    res.append(tag)
                    open_tags.pop()
                    local_buf = texts.pop()
            else:
                close_tag_callback()
        else:
            local_buf += tmp_str[IDX]
            IDX += 1

    if len(close_tags) != 0:
        raise RuntimeError(
            f"Закрывающий тег {close_tags[0]} не имеет открывающего тэга"
        )
    return res


def open1():
    print("Open tag")


def close1():
    print("Close tag")


def data1():
    print("Close tag")


if __name__ == "__main__":
    TEXT1 = """<!DOCTYPE html>
            <html>
            <head>
                <title>Заголовки и абзацы</title>
                <meta charset="utf-8">
            </head>
            <body>
                <h1>Заголовок<br>первого уровня</h1>
                <h2>Заголовок второго уровня</h2>
                <h3>Заголовок третьего уровня</h3>
                <h4>Заголовок четвертого уровня</h4>
                <h5>Заголовок пятого уровня</h5>
                <h6>Заголовок шестого уровня</h6>
                <hr>
                <p>Тест абзаца</p>
            </body>
            </html>"""
    TEXT2 = """<!DOCTYPE html>
        <html>
        <head>
            <title>Заголовки и абзацы</title>
            <meta charset="utf-8">
        </head>
        <body>
            Заголовок<br>первого уровня</h1>
            <h2>Заголовок второго уровня</h2>
            <h3>Заголовок третьего уровня</h3>
            <h4>Заголовок четвертого уровня</h4>
            <h5>Заголовок пятого уровня</h5>
            <h6>Заголовок шестого уровня</h6>
            <hr>
            <p>Тест абзаца</p>
        </body>
        </html>"""
    try:
        print("Example1-----------------------------------------")
        res1 = parse_html(TEXT1, open1, data1, close1)
        print(res1)
        print("Example2(incorrect)-----------------------------------------")
        res2 = parse_html(TEXT2, open1, data1, close1)
        print(res2)
    except (RuntimeError, ValueError) as er:
        print(er)
