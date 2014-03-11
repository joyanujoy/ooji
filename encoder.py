"""
Encoder class provides methods to
    - encode given integer to any base, default base62
    - decode given word to an integer
"""

DFLT_GLYPHS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'


def is_valid(glyph_str):
        uniq = True
        # len(unique Set()) == len(str) ?
        if len({x for x in glyph_str}) != len(glyph_str):
            uniq = False

        return uniq and glyph_str.isalnum()


class Encoder(object):
    
    def __init__(self, glyphs=DFLT_GLYPHS):
        pass

