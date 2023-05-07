import pytest
from datetime import datetime
from medlog.adapters.repository import SqlAlchemyRepository
from medlog.domain.models import Bookmark

pytestmark = pytest.mark.usefixtures("mappers")


def test_add_dailylog(sqlite_session_factory):
    session = sqlite_session_factory()
    repo = SqlAlchemyRepository(session)
    m1 = Bookmark(
        medid=1,
        medname=f"Heart Med #3",
        amount=int(1),
        date_added=datetime(2023, 8, 12),
        date_edited=datetime(2023, 8, 12),
    )
    repo.add_one(m1)
    assert repo.get(m1.id) == m1
