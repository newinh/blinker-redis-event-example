from app.event import EventType, Event
from app import dispatcher


class NoticeRepository(object):

    def delete(self, notice_id: int):
        print('notice will be deleted.')
        event = Event(EventType.NOTICE_DELETED, {'notice_id': notice_id})
        dispatcher.source(event)
