from .repository import CommentRepository


class CommentResource(object):

    def delete(self):
        CommentRepository().delete()
        pass
