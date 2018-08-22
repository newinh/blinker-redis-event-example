from app.dispatcher import Dispatcher, Event


class NoticeRepository(object):

    def delete(self):
        print('notice will be deleted.')
        Dispatcher.source(Event.NOTICE_DELETED)
