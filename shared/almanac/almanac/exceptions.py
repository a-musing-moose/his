class ServiceNotFoundError(Exception):
    """Rasied when a requested contract cannot be matched"""

    def __init__(self, contract_name: str) -> None:
        super().__init__("No registered service found for the contract {}".format(contract_name))


class InvalidServiceType(Exception):
    """Raised when attempting to register a services with no contract"""

    def __init__(self, service_class) -> None:
        super().__init__("{} does not extend an abstract base contract".format(service_class.__name__))


class InvalidContract(Exception):
    """Raised when requested contract is not a contract"""

    def __init__(self, contract) -> None:
        name = getattr(contract, '__name__', str(contract))
        super().__init__("{} is not a contract".format(name))
