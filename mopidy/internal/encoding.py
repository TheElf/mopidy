from __future__ import absolute_import, unicode_literals

import locale

from mopidy import compat


def locale_decode(obj):
    if isinstance(obj, compat.text_type):
        return obj
    elif isinstance(obj, bytes):
        return obj.decode(locale.getpreferredencoding())
    else:
        if compat.PY2:
            return str(obj).decode(locale.getpreferredencoding())
        else:
            return str(obj)
