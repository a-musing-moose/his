import logging
from gettext import gettext as _
from typing import Generator

from autobahn.asyncio.wamp import ApplicationSession  # type: ignore
from autobahn.wamp import RegisterOptions  # type: ignore
from schematics.models import Model

from shopping import actions

log = logging.getLogger('shopping')


class Shopping(ApplicationSession):

    ACTION_PREFIX = 'shopping'

    async def onJoin(self, details) -> Generator:
        log.debug(_("Connected to WAMP Router"))
        self.running = True

        for action_name in actions.__all__:
            name = "{}.{}".format(self.ACTION_PREFIX, action_name)
            action = getattr(actions, action_name)
            handler = self._build_handler(action)

            await self.register(
                handler,
                name,
                RegisterOptions(invoke='random')
            )
            log.debug(_("Registered {} in shared mode").format(name))

    def _build_handler(self, action):
        """Build a handler for the action with automatic serialization"""

        async def handler(*args, **kwargs):
            # Wraps the action with some serialization
            response = await action(*args, **kwargs)
            if isinstance(response, list):
                return [item.to_primitive() for item in response]
            elif isinstance(response, Model):
                return response.to_primitive()
            return response  # lets hope it is a primitive type shall we...
        return handler
