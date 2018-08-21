from . import modified_notice_event_broker, deleted_notice_event_broker

from redis_project.event_broker import fredis


class NoticeRepository(object):
    def delete(self):
        print('notice will be deleted.')
        # deleted_notice_event_broker.send('delete_notice')
        fredis.lpush("dbtool:event", "test")
        pass
