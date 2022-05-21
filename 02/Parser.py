max_len = 0
index = 0:
    
def parse_open_tag(html_str: str):
    global max_len
    global index
    if html_str[index] == '/':
        raise RuntimeError("Close tag before open tag")
    else:
        buf = ''
        while  index != max_len and html_str[index] != '>':
            buf += html_str[index]
            index += 1
        index += 1
    if index == max_len:
        raise RuntimeError("expected >")
    return buf

def parse_close_tag(html_str: str):
    global max_len
    global index
    buf = ''
    while index != max_len and html_str[index] != '>':
        buf += html_str[index]
        index += 1
    if index == max_len:
        raise RuntimeError("expected >")
    return buf

def parse_text(html_str: str):
    global max_len
    global index
    buf = ''
    while index != max_len  and (html_str[index] != '<' or html_str[index + 1] != '/'):
        if index == '<':
            
        buf += html_str[index]
        index += 1
    if index == max_len:
        raise RuntimeError("expected close_tag")
    return buf
def parse_html(html_str: str, open_tag_callback, data_callback, close_tag_callback):
    global max_len
    global index
    max_len = len(html_str)
    while index < max_len:
        if html_str[index] == ' ':
            index += 1
            continue
        if html_str[index] == '<':
            index += 1
            open_ = parse_open_tag(html_str)
            open_tag_callback(open_)
            data_callback(parse_data(html_str))
            close_ = parse_close_tag(html_str)
            open_tag_callback()
            if open_ != close:
                raise RuntimeError("Different tags")
        else:
            raise RuntimeError("Wrong symbol")
            
                