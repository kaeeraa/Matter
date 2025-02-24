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
from matter.core.classes.i18n import tr
from matter.core.classes.logger import logger
from matter.core.classes.ticket import Ticket
from matter.core.classes.tickets.ticketManager import TicketManager

COMMAND_NAME = "new"
COMMAND_DESCRIPTION: str = tr("Create a new ticket")


@slash_command(name="new", description=COMMAND_DESCRIPTION)
async def newTicket(
    ctx: GatewayContext,
    title: Option[str, str] = "Ndfined",
    description: Option[str, str] = "None"
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
    logger.trace(tr("/{command} command called ({author})").format(command=COMMAND_NAME, author=ctx.author.username))
    # Return config fully
    _config: dict[str, Any] = Config().getDictionary("")
    _ticket: Ticket = TicketManager().newTicket(author=ctx.author, title=title, description=description)

    if guild := ctx.get_guild():
        name: str = _config.get("brain.tickets.format", "{username}-{counter}")

        formattedName: str = name.format(username=_ticket.author.username, counter=_ticket.ticketId)

        await guild.create_text_channel(
            name=formattedName,
            topic=_ticket.description,
            category=_config.get("brain.tickets.category_id", None),
            reason=tr("New ticket by {author}").format(author="ctx.author.username"),
        )

        await ctx.respond(tr("Ticket created successfully!"))
        return
    raise RuntimeError()
