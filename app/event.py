from enum import Enum
import json


class EventType(Enum):
    NOTICE_DELETED = 'NOTICE_DELETE'
    NOTICE_MODIFIED = 'NOTICE_MODIFIED'


class Event(object):

    def __init__(self, event_type: EventType, data: dict):
        self.type = event_type
        self.data = data

    @classmethod
    def load(cls, serialized):
        serialized = json.loads(serialized)
        type_ = EventType(serialized['type'])
        return cls(type_, serialized['data'])

    def serialize(self):
        obj = vars(self)
        obj['type'] = self.type.value
        return json.dumps(obj)

    def publish(self):
        if self.type == EventType.NOTICE_DELETED:
            notice_id = self.data.get('notice_id')

            # TODO: use dispatcher?
            import blinker
            blinker.signal(self.type.value).send("i'm sender", notice_id=notice_id)
