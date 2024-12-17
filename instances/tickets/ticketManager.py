"""
Manages tickets.

This class contains methods to create, manage and get tickets.
"""
from hikari import User
from classes.ticket import Ticket


class TicketManager:
    """
    Manages tickets.

    This class contains methods to create, manage and get tickets.
    """

    def __init__(self):
        self.tickets = []

    def newTicket(self, author: User, title: str, description: str) -> Ticket:
        """
        Creates a new ticket and adds it to the list of tickets.

        Args:
            author (hikari.User): The author of the ticket.
            title (str): The title of the ticket.
            description (str): The description of the ticket.

        Returns:
            Ticket: The newly created ticket.
        """
        ticket = Ticket(len(self.tickets) + 1, author, author.id, title, description)
        self.tickets.append(ticket)

        return ticket

    def getTickets(self) -> list:
        """
        Returns the list of tickets.

        Returns:
            list: The list of tickets.
        """
        return self.tickets

    def getTicketById(self, ticketId: int) -> Ticket | None:
        """
        Returns the ticket with the specified ID.

        Args:
            ticketId (int): The ID of the ticket to return.

        Returns:
            Ticket: The ticket with the specified ID, or None if not found.
        """
        for ticket in self.tickets:
            if ticket.ticketId == ticketId:
                return ticket

        return None

    def removeTicket(self, ticketId: int) -> bool:
        """
        Removes a ticket from the list of tickets.

        Args:
            ticketId (int): The ID of the ticket to remove.

        Returns:
            bool: True if the ticket was removed, False otherwise.
        """
        if ticket := self.getTicketById(ticketId):
            self.tickets.remove(ticket)
            return True

        return False
