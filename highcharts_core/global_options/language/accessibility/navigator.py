from typing import Optional

from validator_collection import validators

from highcharts_core.metaclasses import HighchartsMeta


class NavigatorLanguageOptions(HighchartsMeta):
    """Language options for the navigator when used in accessibility mode."""

    def __init__(self, **kwargs):
        self._change_announcement = None
        self._group_label = None
        self._handle_label = None
        
        self.change_announcement = kwargs.get('change_announcement', None)
        self.group_label = kwargs.get('group_label', None)
        self.handle_label = kwargs.get('handle_label', None)

    @property
    def change_announcement(self) -> Optional[str]:
        """Announcement for assistive technology when navigator values
        are changed. Defaults to ``'{axisRangeDescription}'``.
        
        .. note::
        
          Receives ``axisRangeDescription`` and ``chart`` as context, where
          ``axisRangeDescription`` corresponds to the range description
          defined in 
          :class:`AxisLanguageOptions <highcharts_core.global_options.language.accessibility.axis.AxisLanguageOptions>
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._change_announcement

    @change_announcement.setter
    def change_announcement(self, value):
        if value is None:
            self._change_announcement = None
        else:
            self._change_announcement = validators.string(value, allow_empty = True)
            
    @property
    def group_label(self) -> Optional[str]:
        """Label for the navigator region. Defaults to ``'Axis zoom'``.
        
        .. note::
          
          Receives ``chart`` as context.
          
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`        
        """
        return self._group_label
    
    @group_label.setter
    def group_label(self, value):
        if value is None:
            self._group_label = None
        else:
            self._group_label = validators.string(value, allow_empty = True)
            
    @property
    def handle_label(self) -> Optional[str]:
        """Label for the navigator handles. Defaults to 
        ``'{#eq handleIx 0}Start, percent{else}End, percent{/eq}'``.
        
        .. note::
        
          Receives ``handleIx`` and ``chart`` as context, where 
          ``handleIx`` refers to the index of the navigator handle.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`        
        """
        return self._handle_label
    
    @handle_label.setter
    def handle_label(self, value):
        if value is None:
            self._handle_label = None
        else:
            self._handle_label = validators.string(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'change_announcement': as_dict.get('changeAnnouncement', None),
            'group_label': as_dict.get('groupLabel', None),
            'handle_label': as_dict.get('handleLabel', None),
        }
        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'changeAnnouncement': self.change_announcement,
            'groupLabel': self.group_label,
            'handleLabel': self.handle_label,
        }

        return untrimmed
