import pytest
import asyncio


@pytest.fixture(scope="module")
def loop():
    loop = asyncio.get_event_loop()
    import psql
    psql.start_db(None,None)
    yield loop
    psql.stop_db(None,None)