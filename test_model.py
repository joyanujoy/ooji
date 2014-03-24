# -*- coding: utf-8 -*-
from model import Request, Url, Model
import urllib2


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
        urls = [u'http://python.org', u'http://python.org', u'http://google.com']

        for url in urls:
            url_enc = urllib2.quote(url.encode('utf8'))
            id = m.add_url(url_enc)
            assert isinstance(id, int)

    def test_mode_query_url(self):
        m = Model('postgresql', 'ajoy', 'ajoy', 'localhost', '5432', 'ajoy')
        urls = [u'http://python.org', u'http://python.org',
                u'http://google.com',
                u'http://example.com/düsseldorf?neighbourhood=Lörick']
        for url in urls:
            url_enc = urllib2.quote(url.encode('utf8'))
            id = m.add_url(url_enc)
            url_from_query = m.query_url(id)
            assert url_from_query == url_enc
