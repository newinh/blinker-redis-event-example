from app.notice.controller import NoticeResource
from app.comment.controller import CommentResource
from app.attachment.controller import AttachmentResource

from app.dispatcher import run_event_handling_loop

if __name__ == '__main__':

    with run_event_handling_loop():
        NoticeResource().delete()
        NoticeResource().delete()
        NoticeResource().delete()

