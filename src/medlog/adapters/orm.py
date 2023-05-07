import logging
from typing import Text
from sqlalchemy import (
    Table,
    MetaData,
    Column,
    Integer,
    String,
    DateTime,
    Text,
    event,
)
from sqlalchemy.log import InstanceLogger

from sqlalchemy.orm import registry, mapper, relationship

from medlog.domain.models import Bio, DailyLog
logger = logging.getLogger(__name__)

metadata = MetaData()

mapper_registry = registry()
Base = mapper_registry.generate_base()


"""
Pure domain bookmark:
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
url TEXT NOT NULL,
notes TEXT,
date_added TEXT NOT NULL
date_edited TEXT NOT NULL
"""
bio = Table(
    "bio",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("user", String(255)),
    Column("adddate", DateTime),
    Column("editdate", DateTime),
)

dailylog = Table(
    "dailylog",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("medid", Integer),
    Column("medname", String(255)),
    Column("amount", Integer),
    Column("adddate", DateTime),
    Column("editdate", DateTime),
)


def start_mappers():
    logger.info("starting mappers")
    bio_mapper = mapper(Bio, bio)


def start_mappers():
    logger.info("starting mappers")
    dailylog_mapper = mapper(DailyLog, dailylog)
