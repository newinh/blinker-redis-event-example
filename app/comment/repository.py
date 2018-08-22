from app.dispatcher import Dispatcher, Event


class CommentRepository:

    @Dispatcher.register(Event.NOTICE_DELETED)
    def delete(self):
        a = 3
        print('comment deleted')
