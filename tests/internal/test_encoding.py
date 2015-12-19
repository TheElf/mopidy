# encoding: utf-8

from __future__ import absolute_import, unicode_literals

import unittest

import mock

from mopidy import compat
from mopidy.internal import encoding


@mock.patch('mopidy.internal.encoding.locale.getpreferredencoding')
class LocaleDecodeTest(unittest.TestCase):

    def test_can_decode_utf8_strings_with_french_content(self, mock):
        mock.return_value = 'UTF-8'

        result = encoding.locale_decode(
            '[Errno 98] Adresse déjà utilisée'.encode('utf-8'))

        self.assertEqual('[Errno 98] Adresse déjà utilisée', result)

    def test_can_decode_an_ioerror_with_french_content(self, mock):
        mock.return_value = 'UTF-8'

        if compat.PY2:
            error = IOError(98, 'Adresse déjà utilisée'.encode('utf-8'))
        else:
            error = IOError(98, 'Adresse déjà utilisée')
        result = encoding.locale_decode(error)
        expected = '[Errno 98] Adresse déjà utilisée'

        self.assertEqual(
            expected, result,
            '%r decoded to %r does not match expected %r' % (
                error, result, expected))

    def test_does_not_use_locale_to_decode_unicode_strings(self, mock):
        mock.return_value = 'UTF-8'

        encoding.locale_decode('abc')

        self.assertFalse(mock.called)

    def test_does_use_locale_to_decode_ascii_bytestrings(self, mock):
        mock.return_value = 'UTF-8'

        encoding.locale_decode(b'abc')

        mock.assert_called_once_with()
