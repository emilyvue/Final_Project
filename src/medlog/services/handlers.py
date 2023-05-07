from __future__ import annotations
from dataclasses import asdict
from typing import List, Dict, Callable, Type, TYPE_CHECKING

from medlog.domain import commands, events, models

if TYPE_CHECKING:
    from . import unit_of_work


def add_to_dailylog(
    cmd: commands.AddDailyLogCommand,
    uow: unit_of_work.AbstractUnitOfWork,
):
    with uow:

        DailyLog = None

        try:
            DailyLog = uow.dailylogs.get_by_title(value=cmd.title)

            if not DailyLog:
                DailyLog = models.DailyLog(
                    cmd.id, cmd.medid, cmd.medname, cmd.amount, cmd.adddate, cmd.editdate,
                )
                uow.DailyLogs.add(DailyLog)
        except:
            DailyLog = models.DailyLog(
                cmd.id, cmd.medid, cmd.medname, cmd.amount, cmd.adddate, cmd.editdate,
            )
            uow.DailyLogs.add(DailyLog)

        uow.commit()

# ListBookmarksCommand: order_by: str order: str


def list_dailylogs(
    cmd: commands.ListDailyLogCommand,
    uow: unit_of_work.AbstractUnitOfWork,
):
    DaliyLogs = None
    with uow:
        DailyLogs = uow.DailyLogs.all()

    return DailyLogs


def edit_dailylog(
    cmd: commands.UpdateDailyLogCommand,
    uow: unit_of_work.AbstractUnitOfWork,
):
    with uow:
        pass


def delete_dailylog(
    cmd: commands.DeleteDailyLogCommand,
    uow: unit_of_work.AbstractUnitOfWork,
):
    with uow:
        pass


EVENT_HANDLERS = {
    events.DailyLogAdded: [add_to_dailylog],
    events.DailyLogListed: [list_dailylogs],
    events.DailyLogDeleted: [delete_dailylog],
    events.DailyLogUpdated: [edit_dailylog],
}

COMMAND_HANDLERS = {
    commands.AddDailyLogCommand: add_to_dailylog,
    commands.ListDailyLogCommand: list_dailylogs,
    commands.DeleteDailyLogCommand: delete_dailylog,
    commands.UpdateDailyLogCommand: edit_dailylog,
}
