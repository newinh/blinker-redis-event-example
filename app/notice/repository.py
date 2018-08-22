from app.dispatcher import Dispatcher, EventType, Event


class NoticeRepository(object):

    def delete(self, notice_id: int):
        print('notice will be deleted.')
        event = Event(EventType.NOTICE_DELETED, {'notice_id': notice_id})
        Dispatcher.source(event)
