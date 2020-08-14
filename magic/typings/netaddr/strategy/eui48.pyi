"""
This type stub file was generated by pyright.
"""

import re as _re

"""
IEEE 48-bit EUI (MAC address) logic.

Supports numerous MAC string formats including Cisco's triple hextet as well
as bare MACs containing no delimiters.
"""
width = 48
family = AF_LINK
family_name = 'MAC'
version = 48
max_int = 2 ** width - 1
class mac_eui48(object):
    """A standard IEEE EUI-48 dialect class."""
    word_size = ...
    num_words = ...
    max_word = ...
    word_sep = ...
    word_fmt = ...
    word_base = ...


class mac_unix(mac_eui48):
    """A UNIX-style MAC address dialect class."""
    word_size = ...
    num_words = ...
    word_sep = ...
    word_fmt = ...
    word_base = ...


class mac_unix_expanded(mac_unix):
    """A UNIX-style MAC address dialect class with leading zeroes."""
    word_fmt = ...


class mac_cisco(mac_eui48):
    """A Cisco 'triple hextet' MAC address dialect class."""
    word_size = ...
    num_words = ...
    word_sep = ...
    word_fmt = ...
    word_base = ...


class mac_bare(mac_eui48):
    """A bare (no delimiters) MAC address dialect class."""
    word_size = ...
    num_words = ...
    word_sep = ...
    word_fmt = ...
    word_base = ...


class mac_pgsql(mac_eui48):
    """A PostgreSQL style (2 x 24-bit words) MAC address dialect class."""
    word_size = ...
    num_words = ...
    word_sep = ...
    word_fmt = ...
    word_base = ...


DEFAULT_DIALECT = mac_eui48
RE_MAC_FORMATS = ('^' + ':'.join(['([0-9A-F]{1,2})'] * 6) + '$', '^' + '-'.join(['([0-9A-F]{1,2})'] * 6) + '$', '^' + ':'.join(['([0-9A-F]{1,4})'] * 3) + '$', '^' + '-'.join(['([0-9A-F]{1,4})'] * 3) + '$', '^' + r'\.'.join(['([0-9A-F]{1,4})'] * 3) + '$', '^' + '-'.join(['([0-9A-F]{5,6})'] * 2) + '$', '^' + ':'.join(['([0-9A-F]{5,6})'] * 2) + '$', '^(' + ''.join(['[0-9A-F]'] * 12) + ')$', '^(' + ''.join(['[0-9A-F]'] * 11) + ')$')
RE_MAC_FORMATS = [_re.compile(_, _re.IGNORECASE) for _ in RE_MAC_FORMATS]
def valid_str(addr):
    """
    :param addr: An IEEE EUI-48 (MAC) address in string form.

    :return: ``True`` if MAC address string is valid, ``False`` otherwise.
    """
    ...

def str_to_int(addr):
    """
    :param addr: An IEEE EUI-48 (MAC) address in string form.

    :return: An unsigned integer that is equivalent to value represented
        by EUI-48/MAC string address formatted according to the dialect
        settings.
    """
    ...

def int_to_str(int_val, dialect=...):
    """
    :param int_val: An unsigned integer.

    :param dialect: (optional) a Python class defining formatting options.

    :return: An IEEE EUI-48 (MAC) address string that is equivalent to
        unsigned integer formatted according to the dialect settings.
    """
    ...

def int_to_packed(int_val):
    """
    :param int_val: the integer to be packed.

    :return: a packed string that is equivalent to value represented by an
    unsigned integer.
    """
    ...

def packed_to_int(packed_int):
    """
    :param packed_int: a packed string containing an unsigned integer.
        It is assumed that string is packed in network byte order.

    :return: An unsigned integer equivalent to value of network address
        represented by packed binary string.
    """
    ...

def valid_words(words, dialect=...):
    ...

def int_to_words(int_val, dialect=...):
    ...

def words_to_int(words, dialect=...):
    ...

def valid_bits(bits, dialect=...):
    ...

def bits_to_int(bits, dialect=...):
    ...

def int_to_bits(int_val, dialect=...):
    ...

def valid_bin(bin_val, dialect=...):
    ...

def int_to_bin(int_val):
    ...

def bin_to_int(bin_val):
    ...

