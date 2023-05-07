from __future__ import annotations
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from typing import Dict, List
import pytest
from medlog.domain import commands, models
from medlog.services import handlers, unit_of_work
from medlog.adapters import repository

from medlog.adapters.orm import start_mappers


def test_adding_record_to_dailylog(session):
    x = models.DailyLog(1, 20, "spinachrolls", 100, 10)

    x_repository = repository.SqlAlchemyRepository(session)
    x_repository.add(x)
    session.commit()

    rows = session.execute(
        'SELECT ID , medid, medname, amount FROM "dailylog"'
    )
    assert list(rows) == [(1, 20, "heart medicine #1", 1)]
