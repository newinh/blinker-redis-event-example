from redis_project.notice.controller import NoticeResource
from redis_project.comment.controller import CommentResource
from redis_project.attachment.controller import AttachmentResource

import redis_project.dispatcher

if __name__ == '__main__':
    result = NoticeResource().delete()
    NoticeResource().delete()
    NoticeResource().delete()
    print(result)