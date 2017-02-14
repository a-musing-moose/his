from inspect import getmro, isabstract
from typing import Any

from .exceptions import (
    InvalidContract,
    InvalidServiceType,
    ServiceNotFoundError,
)


class Services(object):
    """A services registry"""

    def __init__(self) -> None:
        self._services = {}  # type: dict

    def _get_contract_name(self, cls: type) -> str:
        for name in (c.__name__ for c in getmro(cls) if isabstract(c)):
            return name
        raise InvalidServiceType(cls)

    def register(self, service: Any) -> None:
        contract_name = self._get_contract_name(type(service))
        self._services[contract_name] = service

    def get(self, contract: type) -> Any:
        if not isinstance(contract, type) or not isabstract(contract):
            raise InvalidContract(contract)
        contract_name = contract.__name__
        if contract_name not in self._services:
            raise ServiceNotFoundError(contract_name)
        return self._services[contract_name]


services = Services()
