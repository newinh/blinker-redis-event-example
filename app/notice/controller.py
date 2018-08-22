from .repository import NoticeRepository


class NoticeResource():

    def delete(self, notice_id: int):
        # ...
        NoticeRepository().delete(notice_id)
        # ...