"""This module contains the embed helper functions."""

from datetime import datetime

from arc import GatewayContext
from hikari import Color
from hikari.embeds import Embed


def new_embed(ctx: GatewayContext, title: str, description: str) -> Embed:
    """
    Creates and returns a new Embed object.

    Args:
        ctx (GatewayContext): The context that invoked this command, used for author details.
        title (str): The title of the embed.
        description (str): The description of the embed.

    Returns:
        Embed: A newly created Embed object with the specified title, description, and a footer
        indicating the author and current time.
    """
    embed: Embed = Embed(
        title=title,
        description=description,
        color=Color.from_rgb(90, 0, 240),
    )
    embed.set_footer(
        text=f"Matter  •  Called by @{ctx.author.username}  •  {datetime.now().strftime('%H:%M:%S')}",
        icon=ctx.author.avatar_url,
    )
    return embed
