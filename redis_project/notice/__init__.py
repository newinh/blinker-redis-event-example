import blinker


deleted_notice_event_broker = blinker.signal('DELETED_NOTICE')
modified_notice_event_broker = blinker.signal('MODIFIED_NOTICE')

from .controller import NoticeResource

