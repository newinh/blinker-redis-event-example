# appfrom app.blinker import event_broker
# from .repository import CommentRepository
#
#
# @event_broker.connect
# def receive_data(sender, **kw):
#     print("Caught signal from %r, data %r" % (sender, kw))
#     return 'received!'
#
#
#

# from app import app
from .controller import CommentResource

# app.add_
