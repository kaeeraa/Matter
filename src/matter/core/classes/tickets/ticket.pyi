from datetime import datetime
from enum import Enum
from typing import Any, Optional

from hikari import GuildTextChannel, User as User

class Status(Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    CLOSED = "closed"

class Ticket(object):
    ticketId: int
    channel: GuildTextChannel
    topic: str
    author: User
    status: Status
    createdAt: datetime
    updatedAt: datetime
    def __init__(self, ticketId: int, topic: str, author: User, status: Status = ...) -> None: ...
    def update(self, status: Optional[Status]) -> None: ...
    def dictImpl(self) -> dict[str, Any]: ...
