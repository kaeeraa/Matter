"""This module contains the embed helper functions."""

from datetime import datetime

from arc import GatewayContext
from hikari import Color
from hikari.embeds import Embed


def new_embed(ctx: GatewayContext, title: str, description: str) -> Embed:
    """
    Generate a new Embed object with specified title and description.

    Args:
        ctx (GatewayContext): Context of the command invocation for author details.
        title (str): Title of the embed.
        description (str): Description content of the embed.

    Returns:
        Embed: An Embed object initialized with the provided title, description,
        and a footer showing the author's name and the current time.
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
