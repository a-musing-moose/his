from logging import config

from almanac import services
from autobahn.asyncio.wamp import ApplicationRunner
from wamp.conf import settings
from wamp.service import Shopping

from shopping.repositories import MemoryListItemRepository

if __name__ == '__main__':
    config.dictConfig(settings.LOGGING)
    database_dsn = settings.DATABASE_DSN
    if database_dsn:
        raise Exception("NO IMPLEMENTED YET")
    else:
        item_repo = MemoryListItemRepository()
    services.register(item_repo)

    runner = ApplicationRunner(
        settings.AUTOBAHN_ROUTER,
        settings.AUTOBAHN_REALM
    )
    runner.run(Shopping)
