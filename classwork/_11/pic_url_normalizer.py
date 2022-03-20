def normalize_url(url, domain):
    normalized_url = url
    if url[0] == 'h':
        normalized_url = url
    elif url[0] == '/':
        normalized_erl = 'https://' + domain + url
    elif url[1] == '/':
        normalized_url = 'https:' + url
    return normalized_url
