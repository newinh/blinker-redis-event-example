from app import dispatcher
from app.event import EventType


class AttachmentRepository:

    @dispatcher.subscribe(EventType.NOTICE_DELETED)
    def delete_by_notice_id(self, notice_id: int):
        print(f'Attachments in [{notice_id}] Notice deleted')
