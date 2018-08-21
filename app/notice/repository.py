from . import modified_notice_event_broker, deleted_notice_event_broker

from app.event_broker import fredis


class NoticeRepository(object):
    def delete(self):
        print('notice will be deleted.')
        from blinker import signal
        signal('').send()
        # deleted_notice_event_broker.send('delete_notice')
        fredis.lpush("dbtool:event", "test")
        pass
