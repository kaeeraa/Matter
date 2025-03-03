from hikari import Color, User
from hikari.embeds import Embed

EMBED_COLOR: Color
TIME_FORMAT: str


def embed(author: User, title: str, description: str, color: Color | None = ...) -> Embed: ...
