"""
A slash command to create a new ticket.

This command allows users to create new tickets directly from Discord.
It will create a new ticket in the database and send a message to the channel
with the ticket details.

Example:
    /new test ticket This is a test ticket
"""

from typing import Any

from arc import GatewayContext, Option, slash_command

from matter.core.classes.config import Config
from matter.core.classes.logger import logger
from matter.core.classes.ticket import Ticket
from matter.core.classes.tickets.ticketManager import TicketManager

COMMAND_NAME = "new"
COMMAND_DESCRIPTION = "Create a new ticket"


@slash_command(name="new", description="Create a new ticket")
async def newTicket(
    ctx: GatewayContext, title: Option[str, str] = "Ndfined", description: Option[str, str] = "None"
) -> None:
    """
    Creates a new ticket and sends a message to the channel.

    Args:
        ctx (GatewayContext): The context of the command invocation.
        title (str): The title of the ticket.
        description (str): The description of the ticket.

    Returns:
        None
    """
    logger.trace(f"/new command called ({ctx.author.username})")
    _config: dict[str, Any] = Config().getConfig()
    _ticket: Ticket = TicketManager().newTicket(ctx.author, title, description)

    if guild := ctx.get_guild():
        name: str = _config.get("brain.tickets.format", "{username}-{counter}")

        formattedName: str = name.format(username=_ticket.author.username, counter=_ticket.ticketId)

        await guild.create_text_channel(
            name=formattedName,
            topic=_ticket.description,
            category=_config.get("brain.tickets.category_id", None),
            reason=f"New ticket by {ctx.author.username}",
        )

        await ctx.respond("Ticket created successfully!")
        return
    raise RuntimeError()
