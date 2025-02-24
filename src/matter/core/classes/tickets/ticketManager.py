"""
Manages tickets.

This class contains methods to create, manage and get tickets.
"""

from typing import Any, Optional, cast

from hikari import User

from matter.core.classes.data import Data
from matter.core.classes.ticket import Ticket


class TicketManager(object):
    """
    Manages tickets.

    This class contains methods to create, manage and get tickets.
    """

    _data: Data
    _tickets: dict[str, Any] = {}

    def __init__(self) -> None:
        self._data = Data("tickets")
        self._tickets = self._data.get("tickets", {}) or {}

        if not self._tickets:
            self._data.put("tickets", {})

    def newTicket(self, author: User, title: str, description: str) -> Ticket:

        _ticketsCount: int = len(self._tickets)

        _ticket = Ticket(_ticketsCount + 1, author, author.id, title, description)

        _serialised: dict[str, Any] = {
            "authorId": _ticket.authorId,
            "title": _ticket.title,
            "description": _ticket.description,
            "status": _ticket.status.value,
            "createdAt": _ticket.createdAt,
            "updatedAt": _ticket.updatedAt,
        }

        self._data.put(f"tickets.{_ticket.ticketId}", _serialised)

        return _ticket

    def getTicket(self, ticketId: str) -> Optional[Ticket]:
        """Get ticket from tickets.json5

        Args:
            ticketId (str): an unique ticket id

        Returns:
            Optional[Ticket]: Ticket if exists, None if not exists
        """
        _root: dict[str, Any] = cast(dict[str, Any], self._data.get("", {}))

        return _root.get("tickets", {}).get(ticketId, None)

    def removeTicket(self, ticketId: int) -> None:
        """Remove ticket from tickets.json5

        Args:
            ticketId (int): an unique ticket id
        """
        self._data.remove(f"tickets.{ticketId}")
