from __future__ import absolute_import, unicode_literals

import sys

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

if PY2:
    import ConfigParser as configparser  # noqa
    import Queue as queue  # noqa
    import itertools
    import thread  # noqa

    def fake_python3_urllib_module():
        import types
        import urllib as py2_urllib
        import urlparse as py2_urlparse

        urllib = types.ModuleType(b'urllib')  # noqa
        urllib.parse = types.ModuleType(b'urlib.parse')

        urllib.parse.quote = py2_urllib.quote
        urllib.parse.unquote = py2_urllib.unquote

        urllib.parse.urlparse = py2_urlparse.urlparse
        urllib.parse.urlsplit = py2_urlparse.urlsplit
        urllib.parse.urlunsplit = py2_urlparse.urlunsplit

        return urllib

    urllib = fake_python3_urllib_module()

    integer_types = (int, long)  # noqa
    string_types = (basestring,)  # noqa
    text_type = unicode  # noqa

    input = raw_input  # noqa
    intern = intern  # noqa

    def itervalues(dct, **kwargs):
        return iter(dct.itervalues(**kwargs))

    zip_longest = itertools.izip_longest

else:
    import configparser  # noqa
    import itertools
    import queue  # noqa
    import _thread as thread  # noqa
    import urllib  # noqa

    integer_types = (int,)
    string_types = (str,)
    text_type = str

    input = input
    intern = sys.intern

    def itervalues(dct, **kwargs):
        return iter(dct.values(**kwargs))

    zip_longest = itertools.zip_longest


def with_metaclass(meta, *bases):
    class metaclass(meta):
        def __new__(cls, name, this_bases, d):
            return meta(name, bases, d)
    return type.__new__(metaclass, str('temporary_class'), (), {})
