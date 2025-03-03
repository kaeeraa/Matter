from datetime import datetime
from enum import Enum

from hikari import User as User

class Status(Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    CLOSED = "closed"

class Ticket(object):
    ticketId: int
    author: User
    authorId: int
    title: str
    description: str
    status: Status
    createdAt: datetime
    updatedAt: datetime
    def __init__(
        self, ticketId: int, author: User, authorId: int, title: str, description: str, status: Status = ...
    ) -> None: ...
    def changeStatus(self, status: Status) -> None: ...
