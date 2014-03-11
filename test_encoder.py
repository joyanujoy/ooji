"""
    Test cases for Encoder class
"""
import encoder


class TestEncoder:

    def test_isvalid_default_glyphs(self):
        g = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        assert encoder.is_valid(g)

    def test_isvalid_non_alphanum(self):
        g = 'bcery428)'
        assert False == encoder.is_valid(g)

    def test_isvalid_duplicates(self):
        g = '00123454AA'
        assert False == encoder.is_valid(g)

