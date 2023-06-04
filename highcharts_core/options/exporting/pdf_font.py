from typing import Optional

from validator_collection import validators

from highcharts_core.metaclasses import HighchartsMeta


class PDFFontOptions(HighchartsMeta):
    """Settings for a custom font for the exported PDF, when using the
    ``offline-exporting`` module.

    This is used for languages containing non-ASCII characters, like Chinese, Russian,
    Japanese etc.

    As described in the
    `jsPDF docs <https://github.com/parallax/jsPDF#use-of-unicode-characters--utf-8>`_,
    the 14 standard fonts in PDF are limited to the ASCII-codepage. Therefore, in
    order to support other text in the exported PDF, one or more TTF font files have
    to be passed on to the exporting module.

    """

    def __init__(self, **kwargs):
        self._bold = None
        self._bolditalic = None
        self._italic = None
        self._normal = None

        self.bold = kwargs.get('bold', None)
        self.bolditalic = kwargs.get('bolditalic', None)
        self.italic = kwargs.get('italic', None)
        self.normal = kwargs.get('normal', None)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'exporting.pdfFont'

    @property
    def bold(self) -> Optional[str]:
        """The TTF font file for bold text. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`

        :raises ValueError: if not a URL or path-like string
        """
        return self._bold

    @bold.setter
    def bold(self, value):
        try:
            self._bold = validators.url(value, allow_empty = True)
        except ValueError:
            self._bold = validators.path(value, allow_empty = True)

    @property
    def bolditalic(self) -> Optional[str]:
        """The TTF font file for Bold Italic text. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`

        :raises ValueError: if not a URL or path-like string
        """
        return self._bolditalic

    @bolditalic.setter
    def bolditalic(self, value):
        try:
            self._bolditalic = validators.url(value, allow_empty = True)
        except ValueError:
            self._bolditalic = validators.path(value, allow_empty = True)

    @property
    def italic(self) -> Optional[str]:
        """The TTF font file for italic text. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`

        :raises ValueError: if not a URL or path-like string
        """
        return self._italic

    @italic.setter
    def italic(self, value):
        try:
            self._italic = validators.url(value, allow_empty = True)
        except ValueError:
            self._italic = validators.path(value, allow_empty = True)

    @property
    def normal(self) -> Optional[str]:
        """The TTF font file for normal ``font-style``. Defaults to
        :obj:`None <python:None>`.

        .. note::

           If font variations like bold or italic are not defined, the normal font
           will be used for those, too.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`

        :raises ValueError: if not a URL or path-like string
        """
        return self._normal

    @normal.setter
    def normal(self, value):
        try:
            self._normal = validators.url(value, allow_empty = True)
        except ValueError:
            self._normal = validators.path(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'bold': as_dict.get('bold', None),
            'bolditalic': as_dict.get('bolditalic', None),
            'italic': as_dict.get('italic', None),
            'normal': as_dict.get('normal', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'bold': self.bold,
            'bolditalic': self.bolditalic,
            'italic': self.italic,
            'normal': self.normal
        }

        return untrimmed
