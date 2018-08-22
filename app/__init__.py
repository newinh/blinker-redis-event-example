from flask import Flask

from app.notice.controller import NoticeResource
from app.comment.controller import CommentResource
from app.attachment.controller import AttachmentResource

app = Flask(__name__)


@app.route("/")
def index():
    return "index"


@app.route("/notices/<int:notice_id>", methods=['DELETE'])
def delete_notice(notice_id: int):
    NoticeResource().delete(notice_id)
    return "notice_delete"
