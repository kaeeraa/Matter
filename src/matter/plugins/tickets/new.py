"""A slash command to create a new ticket."""

from typing import Annotated, Any

from arc import GatewayContext, StrParams, slash_command
from hikari import GuildTextChannel

from matter.core.classes.data import Data
from matter.core.classes.i18n import tr
from matter.core.classes.logger import logger
from matter.core.classes.tickets.ticket import Ticket

COMMAND_NAME = "new"
COMMAND_DESCRIPTION: str = tr("Create a new ticket")


@slash_command(name=COMMAND_NAME, description=COMMAND_DESCRIPTION)
async def new(ctx: GatewayContext, topic: Annotated[str, StrParams(tr("Topic of ticket"))]) -> None:
    """Creates a new ticket and sends a message to the channel."""
    logger.trace(tr("/{command} command called ({author})").format(command=COMMAND_NAME, author=ctx.author.username))

    config: dict[str, Any] = Data(isConfig=True).getDict("bot.brain.tickets", {})
    tickets: Data = Data("tickets")
    # count of tickets+1
    _id: int = len(tickets.getDict("tickets", {})) + 1

    ticket: Ticket = Ticket(_id, topic, author=ctx.author)

    if guild := ctx.get_guild():
        name: str = config.get("format", "{username}-{counter}")
        formattedName: str = name.format(username=ticket.author.username, counter=ticket.ticketId)

        channel: GuildTextChannel = await guild.create_text_channel(
            name=formattedName,
            topic=topic,
            category=config.get("category_id", None),
            reason=tr("New ticket by {author}").format(author=ticket.author.username),
        )

        ticket.channel = channel

        tickets.put(path="tickets", data=ticket.dictImpl())

        await ctx.respond(tr("Ticket created successfully!"))
        return

    raise RuntimeError()
