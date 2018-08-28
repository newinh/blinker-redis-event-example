from .repository import AttachmentRepository


class AttachmentResource(object):
    def delete(self):
        AttachmentRepository.delete()
