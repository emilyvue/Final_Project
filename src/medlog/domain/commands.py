
import sys
from abc import ABC
from datetime import datetime
from dataclasses import dataclass
from typing import Optional

import requests


class Command(ABC):
    pass


@dataclass
class AddDailyLogCommand(Command):
    id: int
    medid: int
    medname: str
    amount: int
    adddate: str
    editdate: str


@dataclass
class UpdateDailyLogCommand(Command):
    id: int
    medid: int
    medname: str
    amount: int
    adddate: str
    editdate: str


@dataclass
class ListDailyLogCommand(Command):
    order_by: str
    order: str


@dataclass
class DeleteDailyLogCommand(Command):
    id: int
