from ..notice import deleted_notice_event_broker

class CommentRepository:

    @dispatch.register('EVNET_NAME')
    def delete(self):
        a = 3
        print('comment deleted')
