from model import Request, Url, Model


class TestModel:
    """
        Test cases for Model class
    """

    def test_request_repr(self):
        r = Request('1234-5678')
        s = eval(r.__repr__())
        assert r.url_id == s.url_id == '1234-5678'

    def test_url_repr(self):
        u = Url('1234-5678', 'http://python.org')
        v = eval(u.__repr__())
        assert u.url_text == v.url_text

    def test_model_session(self):
        m = Model('postgresql', 'ajoy', 'ajoy', 'localhost', '5432', 'ajoy')
        assert m.session

    def test_model_add_url(self):
        m = Model('postgresql', 'ajoy', 'ajoy', 'localhost', '5432', 'ajoy')
        urls = ['http://python.org', 'http://python.org', 'http://google.com']
        for url in urls:
            id = m.add_url(url)
            assert isinstance(id, int)

