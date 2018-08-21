from .repository import NoticeRepository


class NoticeResource():
    def delete(self):
        notice_id = 3

        NoticeRepository().delete()
