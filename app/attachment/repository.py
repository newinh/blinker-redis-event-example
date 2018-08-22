from app.dispatcher import Dispatcher, EventType


class AttachmentRepository:

    @Dispatcher.register(EventType.NOTICE_DELETED)
    def delete_by_notice_id(self, notice_id: int):
        print(f'Attachments in [{notice_id}] Notice deleted')
