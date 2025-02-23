"""This module contains the embed helper functions."""

from datetime import datetime
from typing import Optional

from hikari import Color, User
from hikari.embeds import Embed

from matter.core.classes.i18n import tr

EMBED_COLOR = Color.from_rgb(90, 0, 240)
TIME_FORMAT = "%H:%M:%S"


def embed(author: User, title: str, description: str, color: Optional[Color] = EMBED_COLOR) -> Embed:

    _embed: Embed = Embed(
        title=title,
        description=description,
        color=color,
    )

    _footerTemplate: str = tr("Matter  •  Called by @{author}  •  at {date}")

    _footerText = _footerTemplate.format(author=author.username, date=datetime.now().strftime(TIME_FORMAT))

    _embed.set_footer(
        text=_footerText,
        icon=author.avatar_url,
    )

    return _embed
