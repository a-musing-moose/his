Alamanac
========

A simple service registry for use within HIS.

Services registered must extend an abstract base class, which acts as a contract or interface.


Usage
-----

Services should be defined as follows


.. code-block:: python

    import abc

    class ExampleContract(metaclass=abc.ABCMeta):

        @abc.abstractmethod
        def method(self):
            pass


    class ExampleService(ExampleContract):

        def method(self):
            print("I'm an example")


Then register an instance of the service:


.. code-block:: python

    from almanac import services

    s = ExampleService()
    services.register(s)


Finally, to retrieve a registered service you need to use the contract:

.. code-block:: python

    from almanac import services

    s = services.get(ExampleContract)


Errors and Exceptions
---------------------

If you try to register an object as a service which does not have an abstract parent then it will raise an
`InvalidServiceType` exception.

Attempting to get a service which has not been registered will raise a `ServiceNotFoundError` exception.

Attempting to get a service with anything other than an abstract base class (e.g. the contract) will result in the
system raising an `InvalidContract` exception
