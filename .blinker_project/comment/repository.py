from app.blinker.notice import deleted_notice_event_broker, modified_notice_event_broker


class CommentRepository:

    @deleted_notice_event_broker.connect
    def delete(self):
        a = 3
        print('comment deleted')
