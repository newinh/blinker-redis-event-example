from app.dispatcher import Dispatcher, Event


class AttachmentRepository:

    @Dispatcher.register(Event.NOTICE_DELETED)
    def delete(self):
        a = 3
        print('attachment deleted')
