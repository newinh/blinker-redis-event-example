from blinker_project.notice.controller import NoticeResource
from blinker_project.comment.controller import CommentResource
from blinker_project.attachment.controller import AttachmentResource

if __name__ == '__main__':
    result = NoticeResource().delete()
    NoticeResource().delete()
    NoticeResource().delete()
    print(result)