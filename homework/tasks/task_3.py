import asyncio
from dataclasses import dataclass
from typing import Awaitable


@dataclass
class Ticket:
    number: int
    key: str


async def coroutines_execution_order(coros: list[Awaitable[Ticket]]) -> str:

    tickets = await asyncio.gather(*coros)

    sorted_tickets = sorted(tickets, key=lambda ticket: ticket.number)

    result = "".join(ticket.key for ticket in sorted_tickets)

    return result
