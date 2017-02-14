from abc import ABCMeta, abstractmethod

import pytest

from almanac import exceptions
from almanac.registry import Services


class MockContract(metaclass=ABCMeta):

    @abstractmethod
    def m(self):
        ...


class MockService(MockContract):

    def m(self):
        pass


def test_registering_service_without_abc_raises_exception():
    services = Services()
    with pytest.raises(exceptions.InvalidServiceType):
        services.register(object())


def test_gets_correct_contract_name():
    services = Services()
    name = services._get_contract_name(MockService)
    assert name == MockContract.__name__


def test_can_retrieve_register_service_by_contract():
    services = Services()
    service = MockService()
    services.register(service)
    assert service == services.get(MockContract)


def test_retrieving_unregistered_service_raises_an_exception():
    services = Services()
    with pytest.raises(exceptions.ServiceNotFoundError):
        services.get(MockContract)


def test_retrieving_with_non_type_raises_exception():
    services = Services()
    with pytest.raises(exceptions.InvalidContract):
        services.get(object())


def test_retrieving_with_non_contract_class_raises_exception():
    services = Services()
    with pytest.raises(exceptions.InvalidContract):
        services.get(MockService)
