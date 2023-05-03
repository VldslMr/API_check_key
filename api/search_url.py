def search_url(body, pattern):
    body_str = body.decode('utf-8')
    body_list = body_str.split('&')
    body_dict = {}
    for field in body_list:
        split_field = field.split('=')
        body_dict[split_field[0]] = split_field[1]
    return body_dict[pattern]
