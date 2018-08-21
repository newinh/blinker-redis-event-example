from blinker import signal


deleted_notice_event_broker = signal('DELETED_NOTICE')
modified_notice_event_broker = signal('MODIFIED_NOTICE')

from .controller import NoticeResource

