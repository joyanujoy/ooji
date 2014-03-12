"""
Encoder class provides methods to
    - encode given integer to any base, default base62
    - decode given word to an integer
"""

DFLT_GLYPHS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'


def is_valid(glyph_str):
    """ validates if glyph_str is alphanumeric and contains unique chars """
    uniq = True
    if len({x for x in glyph_str}) != len(glyph_str):
        uniq = False

    return uniq and glyph_str.isalnum()


class Encoder(object):
    """
    Encoder class provides methods to
    - encode given integer to any base, default base62
    - decode given word to an integer
    """

    def __init__(self, glyphs=DFLT_GLYPHS):

        if not is_valid(glyphs):
            raise ValueError("Invalid Glyph. Use unique alphanumeric chars")

        self.glyphs = glyphs
        self.base = len(glyphs)

    def encode(self, num):
        """
        @param num : integer
        @returns : encoded number
        """
        if not isinstance(num, int):
            raise TypeError("Invalid number. Enter integer")

        if num == 0:
            return '0'

        stack = []

        while num > 0:
            rem = num % self.base
            stack.append(self.glyphs[rem])
            num //= self.base

        stack.reverse()
        return ''.join(stack)

    def decode(self, word):
        """
        @param word : encoded string
        @returns : decoded decimal integer number
        """
        if not isinstance(word, str):
            raise TypeError("Invalid word. Enter string")

        top_index = len(word) - 1

        num = 0

        for i, char in enumerate(word):
            try:
                p = top_index - i
                num += self.glyphs.index(char) * (self.base ** p)
            except ValueError:
                raise ValueError('{c} not in'
                                 ' glyph:{g}'.format(c=char, g=self.glyphs))
            except:
                raise

        return num
