"""This module contains the Ticket class."""

from datetime import datetime
from enum import Enum
from typing import Any, Optional

from hikari import GuildTextChannel, User


class Status(Enum):
    """This enumeration contains the different statuses that a ticket can have."""

    OPEN = "open"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    CLOSED = "closed"


class Ticket(object):
    """This class represents a ticket and its attributes."""

    def __init__(self, ticketId: int, topic: str, author: User, status: Status = Status.OPEN) -> None:
        self.ticketId: int = ticketId
        self.channel: GuildTextChannel
        self.topic: str = topic
        self.author: User = author
        self.status: Status = status
        self.createdAt: datetime = datetime.now()
        self.updatedAt: datetime = datetime.now()

    def update(self, status: Optional[Status]) -> None:
        """Changes the status of the ticket to the specified status."""
        if status:
            self.status = status
        self.updatedAt = datetime.now()

    def dictImpl(self) -> dict[str, Any]:
        return {
            "id": self.ticketId,
            "channel_id": self.channel.id,
            "name": self.channel.name,
            "topic": self.channel.topic,
            "author_id": self.author.id,
            "status": self.status.value,
            "created_at": self.createdAt,
            "updated_at": self.updatedAt,
        }
