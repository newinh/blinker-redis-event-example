from app.notice.controller import NoticeResource
from app.comment.controller import CommentResource
from app.attachment.controller import AttachmentResource

from app.event import run_event_handling_loop

if __name__ == '__main__':

    with run_event_handling_loop():
        NoticeResource().delete(3)
        NoticeResource().delete(4)
        NoticeResource().delete(5)

