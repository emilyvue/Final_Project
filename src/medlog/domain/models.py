from __future__ import annotations
from dataclasses import dataclass
from datetime import date, datetime
from typing import List, Optional


class Bio:

    def __init__(self, id: int, user: str, adddate: datetime, editdate: datetime):
        self.id: int = id
        self.title: str = user
        self.adddate: str = adddate
        self.editdate: str = editdate
        self.events = []


class DailyLog:

    def __init__(self, id: int, medid: str, medname: str, amount: int, adddate: datetime, editdate: datetime):
        self.id: int = id
        self.medid: str = medid
        self.medname: str = medname
        self.amount: int = amount
        self.adddate: str = adddate
        self.editdate: str = editdate
        self.events = []
