from __future__ import annotations
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from typing import Dict, List
import pytest
from medlog import bootstrap
from medlog.domain import commands
from medlog.services import handlers, unit_of_work
from medlog.adapters import repository

from medlog.adapters.orm import start_mappers
from medlog.services.unit_of_work import AbstractUnitOfWork


def boostrap_test_app():
    return bootstrap.bootstrap(start_orm=False, uow=AbstractUnitOfWork())


def test_add_dailylog_item():

    # arrange
    bus = boostrap_test_app()
    nu: datetime = datetime(2021, 3, 31, 0, 0, 0, 0, tzinfo=timezone.utc)

    # add one = act
    bus.handle(
        commands.AddDailyLogCommand(
            4,
            f"FakeID",  # id medicine
            f"heart medicine #1",  # medicine name
            1,  # amount
            nu.isoformat(),  # date added
            nu.isoformat(),  # date edited
        )
    )

    print(bus.uow.DailyLogs.get_by_medid(f"FakeID"))

    # assert
    assert bus.uow.DailyLogs.get_by_medid(f"FakeID") is not None
    assert bus.uow.committed


def test_get_all_dailylog_records():
    bus = boostrap_test_app()

    nu: datetime = datetime(2021, 3, 31, 0, 0, 0, 0, tzinfo=timezone.utc)
    bus.handle(
        commands.AddDailyLogCommand(
            5,
            f"FakeID",  # id medicine
            f"heart medicine #2",  # medicine name
            1.5,  # amount
            nu.isoformat(),  # date added
            nu.isoformat(),  # date edited
        )
    )

    nuto = nu + timedelta(days=2, hours=12)

    bus.handle(
        commands.AddDailyLogCommand(
            6,
            f"FakeID",  # id medicine
            f"heart medicine #3",  # medicine name
            2,  # amount
            nu.isoformat(),  # date added
            nu.isoformat(),  # date edited
        )
    )

    records = bus.uow.DailyLogs.get_all()
    assert len(records) == 2
