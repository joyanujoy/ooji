# -*- coding: utf-8 -*

DFLT_GLYPHS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'


def is_valid(glyph_str):
    """ Validates if glyph_str is alphanumeric and contains unique chars

    Parameters
    ----------
    glyph_str : string
        glyph alphabet to be used for number encoding

    Returns
    -------
    True when:
        glyph string is alphanumeric
        Each char occurs only once

    """
    uniq = True
    if len({x for x in glyph_str}) != len(glyph_str):
        uniq = False

    return uniq and glyph_str.isalnum()


class Encoder(object):
    """ Encoder class provides methods to
            Encode an integer to any base, default base62
            Decode encoded word to an integer
    Attributes
    ----------
    glyphs : string
        An alphabet to represent numbers. Default is Base62 [a-zA-z0-9]
    base : integer
        Base for number encoding
    """

    def __init__(self, glyphs=DFLT_GLYPHS):

        if not is_valid(glyphs):
            raise ValueError("Invalid Glyph. Use unique alphanumeric chars")

        self.glyphs = glyphs
        self.base = len(glyphs)

    def encode(self, num):
        """ Convert integer to base

        Parameters
        ----------
        num : integer

        Returns
        -------
        word : string
            num is encoded in base and returned as string

        Raises
        ------
        TypeError : Non integer param
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
        """ Decode word to number

        Parameters
        ----------
        word : string
            encoded string

        Returns
        -------
        number : integer
            decoded number

        Raises
        ------
        TypeError : Non string param

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
