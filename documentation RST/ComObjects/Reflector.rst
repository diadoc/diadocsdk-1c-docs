Reflector
=========

Объект для получения информации о других COM-объектах

.. versionadded:: 5.28.7


.. rubric:: Методы

.. tabs::

    .. tab:: Все актуальные

        * :meth:`Reflector.Describe`


.. method:: Reflector.Describe(Object)

    :Object: ``Dispatch`` Com-объект, реализующий интерфейс `IDispatch <https://docs.microsoft.com/en-us/windows/win32/api/oaidl/nn-oaidl-idispatch>`_

    Возвращает :doc:`описание Com-объекта <TypeDesc>`


.. seealso:: :doc:`../HowTo/HowTo_reflect_object`