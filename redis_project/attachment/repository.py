from ..notice import deleted_notice_event_broker



class AttachmentRepository:

    @deleted_notice_event_broker.connect
    def delete(self):
        a = 3
        print('attachment deleted')
