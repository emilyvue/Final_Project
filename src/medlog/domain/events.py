from abc import ABC
from datetime import datetime
from dataclasses import dataclass
from typing import Optional

from .models import DailyLog


class Event(ABC):
    pass


@dataclass
class DailyLogAdded(Event):
    id: int
    medid: int
    medname: str
    amount: int
    adddate: str
    editdate: str


@dataclass
class DailyLogUpdated(Event):
    id: int
    medid: int
    medname: str
    amount: int
    adddate: str
    editdate: str


@dataclass
class DailyLogListed(Event):
    DailyLog: list[DailyLog]


@dataclass
class DailyLogDeleted(Event):
    DailyLog: DailyLog
