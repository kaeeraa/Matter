"""This module contains the embed helper functions."""

from datetime import datetime

from hikari import Color, User
from hikari.embeds import Embed


def newEmbed(author: User, title: str, description: str) -> Embed:
    """
    Generate a new Embed object with specified title and description.

    Args:
        author (User): The user object of the command invoker.
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
        text=f"Matter  •  Called by @{author.username}  •  {datetime.now().strftime('%H:%M:%S')}",
        icon=author.avatar_url,
    )

    return embed
