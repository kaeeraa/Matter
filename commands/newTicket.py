"""
A slash command to create a new ticket.

This command allows users to create new tickets directly from Discord.
It will create a new ticket in the database and send a message to the channel
with the ticket details.

Example:
    /new test ticket This is a test ticket
"""

from arc import Option, slash_command, GatewayContext
from instances.log import logger
from instances.tickets.ticketManager import TicketManager
from instances.config import Config
from helpers.errorHandler import sendError

COMMAND_NAME = "new"
COMMAND_DESCRIPTION = "Create a new ticket"

# mypy: ignore-errors


@slash_command(name="new", description="Create a new ticket")
async def newTicket(ctx: GatewayContext,
                    title: Option[str, str] = "Ndfined",
                    description: Option[str, str] = "None") -> None:
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

    ticket = TicketManager().newTicket(ctx.author, title, description)
    config: dict = Config().getConfig()

    if guild := ctx.get_guild():
        name: str = config.get("brain.tickets.format", "{username}-{counter}")

        formattedName: str = name.format(
            username=ticket.author.username,
            counter=ticket.ticketId
        )

        await guild.create_text_channel(
            name=formattedName,
            topic=ticket.description,
            category=config.get("brain.tickets.category_id", None),
            reason=f"New ticket by {ctx.author.username}"
        )

        await ctx.respond("Ticket created successfully!")
        return
    await sendError(Exception("Guild not found"), ctx, COMMAND_NAME)
