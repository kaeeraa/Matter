from arc import GatewayContext as GatewayContext, Option as Option
from matter.core.classes.config import Config as Config
from matter.core.classes.i18n import tr as tr
from matter.core.classes.logger import logger as logger
from matter.core.classes.ticket import Ticket as Ticket
from matter.core.classes.tickets.ticketManager import TicketManager as TicketManager

COMMAND_NAME: str
COMMAND_DESCRIPTION: str

async def newTicket(ctx: GatewayContext, title: Option[str, str] = 'Ndfined', description: Option[str, str] = 'None') -> None: ...
