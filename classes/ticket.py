"""This module contains the Ticket class."""
from datetime import datetime
from enum import Enum
from hikari import User


class Status(Enum):
    """
    Ticket status enumeration.

    This enumeration contains the different statuses that a ticket can have.
    """
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    CLOSED = "closed"


class Ticket:
    """
    Ticket class.

    This class represents a ticket and its attributes.
    """

    def __init__(self,
                 ticketId: int,
                 author: User,
                 authorId: int,
                 title: str,
                 description: str,
                 status: Status = Status.OPEN):
        self.ticketId = ticketId
        self.author = author
        self.authorId = authorId
        self.title = title
        self.description = description
        self.status = status
        self.createdAt = datetime.now()
        self.updatedAt = datetime.now()

    def changeStatus(self, status: Status):
        """
        Changes the status of the ticket to the specified status.

        Args:
            status (Status): The status to change the ticket to.
        """
        self.status = status
        self.updatedAt = datetime.now()

    def __repr__(self):
        return f"Ticket({self.ticketId}, {self.title}, Status: {self.status})"
