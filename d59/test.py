from typing import List
from uuid import uuid4


class User():
    def __init__(self, id):
        self.user_id = id
        self.slots = dict()
        # all avl
        for i in range(48):
            self.slots[i] = (True, None)

    def get_avl_slots(self):
        ans = []
        for k, v in self.slots:
            if v[0]:
                ans.append(k)
        return ans

    def book_a_slot(self, start, end, meeting_id):
        for i in range(start, end+1):
            self.slots[i] = (False, meeting_id)


class Meeting():
    def __init__(self, start, end):
        self.users = []
        self.start = start
        self.end = end
        self.id = uuid4()

    def invite_users(self, users: List):
        self.users.extend(users)
        trigger_email(users)

    def updateMeeting(self, start, end):
        self.start = start
        self.end = end


def get_availibility_multiple_users(users: List):
    avl_slots = [i for i in range(48)]

    for ele in users:
        for k in avl_slots:
            if not ele.slots[k][0]:
                avl_slots.remove(k)
        if len(avl_slots) == 0:
            return avl_slots
    return avl_slots
