import os
from functools import partial


class env(object):

    def __new__(cls, *args, **kwargs):
        if not args:
            return partial(cls, **kwargs)
        return object.__new__(cls)

    def __init__(self, getter, key=None, parser=None):
        self.getter = getter
        self.parser = parser
        self.key = key or getter.__name__

    def __get__(self, owner, parser=None):
        if owner is None:
            return self
        try:
            value = os.environ[self.key]
        except KeyError:
            value = self.getter(owner)
        else:
            if self.parser:
                value = self.parser(value)
        owner.__dict__[self.getter.__name__] = value
        return value


class Settings(object):

    @env
    def DATABASE_DSN(self):
        return None

    @env
    def AUTOBAHN_ROUTER(self):
        return 'ws://127.0.0.1:8080/ws'

    @env(parser=int)
    def AUTOBAHN_REALM(self):
        return 'realm1'

    @property
    def LOGGING(self):
        return {
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': {
                'simple': {
                    # 'format': '[%(asctime)s][%(levelname)s][%(name)s] %(message)s',
                    'format': (
                        '{{'
                        '"date": "{asctime}", "level": "{levelname}", "name": "{name}", "message": "{message}"'
                        '}}'
                    ),
                    'style': '{'
                }
            },
            'handlers': {
                'console': {
                    'class': 'logging.StreamHandler',
                    'formatter': 'simple'
                },
            },
            'loggers': {
                'shopping': {
                    'handlers': ['console'],
                    'level': 'DEBUG',
                    'propagate': False
                }
            }
        }


settings = Settings()
