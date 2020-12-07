from classwork._11.pic_url_normalizer import normalize_url


def test__normalize_url_1():
    good_url = 'https://http.cat/200.jpg'
    normalized_url = normalize_url('https://http.cat/200.jpg', 'http.cat')
    assert normalized_url == good_url



def test__normalize_url_2():
    good_url = 'https://http.cat/200.jpg'
    normalized_url = normalize_url('//http.cat/200.jpg', 'http.cat')
    assert normalized_url == good_url


def test__normalize_url_3():
    good_url = 'https://http.cat/200.jpg'
    normalized_url = normalize_url('/200.jpg', 'http.cat')
    assert normalized_url == good_url


def test__test_to_fall():
    good_url = 'https://http.cat/200.jpg'
    normalized_url = normalize_url('https://http.cat/200.jpg', 'http.cat')
    assert normalized_url == good_url + 'ERROR'
