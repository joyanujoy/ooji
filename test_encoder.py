"""
    Test cases for Encoder class
"""
from nose.tools import assert_raises, assert_false
import encoder

class TestEncoder:

    def test_isvalid_default_glyphs(self):
        g = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        assert encoder.is_valid(g)

    def test_isvalid_non_alphanum(self):
        g = 'bcery428)'
        assert_false == encoder.is_valid(g)

    def test_isvalid_duplicates(self):
        g = '00123454AA'
        assert_false == encoder.is_valid(g)

    def test_init_invalidglyph(self):
        g = '_111'
        assert_raises(ValueError, encoder.Encoder, g)

    def test_encode_invalid_num(self):
        enc = encoder.Encoder()
        assert_raises(TypeError, enc.encode, 1.0)

    def test_encode_binary(self):
        enc = encoder.Encoder('01')
        assert enc.encode(3) == '11'

    def test_encode_zero(self):
        enc = encoder.Encoder()
        assert enc.encode(0) == '0'

    def test_encode_62(self):
        enc = encoder.Encoder()
        assert enc.encode(61) == 'z'

    def test_decode_not_in_glyph(self):
        """test string with chars not in encoded glyph alphabet"""
        enc = encoder.Encoder()
        assert_raises(ValueError, enc.decode, '@')

    def test_decode_non_string(self):
        enc = encoder.Encoder()
        assert_raises(TypeError, enc.decode, 1)

    def test_decode_binary(self):
        enc = encoder.Encoder(glyphs='01')
        assert enc.decode('11') == 3

    def test_encode_decode_multiple(self):
        enc = encoder.Encoder()
        for num in [0, 10, 50, 100, 1000, 2147483647]:
            enc_word = enc.encode(num)
            dec_num = enc.decode(enc_word)
            assert num == dec_num
