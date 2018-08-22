from app.dispatcher import Dispatcher
from app.event import EventType


class CommentRepository:

    @Dispatcher.register(EventType.NOTICE_DELETED)
    def delete_by_notice_id(self, notice_id: int):
        print(f'Comments in [{notice_id}] Notice deleted')
