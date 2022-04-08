TypeDesc
========

Описание COM-объекта


.. rubric:: Методы

.. tabs::

    .. tab:: Все актуальные

        .. csv-table::
            :header: Информация об интерфейсе, Взаимодействие с полями и метода объекта

            :meth:`TypeDesc.GetInterfaceName`,   :meth:`TypeDesc.SetProperty`
            :meth:`TypeDesc.HasProperty`,        :meth:`TypeDesc.GetProperty`
            :meth:`TypeDesc.GetPropertiesNames`, :meth:`TypeDesc.CreateArgs`
            :meth:`TypeDesc.GetPropertyType`,    :meth:`TypeDesc.InvokeMethod`
            :meth:`TypeDesc.GetMethodsNames`,
            :meth:`TypeDesc.GetMethodDesc`,

    .. tab:: Информация об интерфейсе

        * :meth:`TypeDesc.GetInterfaceName`
        * :meth:`TypeDesc.HasProperty`
        * :meth:`TypeDesc.GetPropertiesNames`
        * :meth:`TypeDesc.GetPropertyType`
        * :meth:`TypeDesc.GetMethodsNames`
        * :meth:`TypeDesc.GetMethodDesc`

    .. tab:: Взаимодействие с полями и метода объекта

        * :meth:`TypeDesc.SetProperty`
        * :meth:`TypeDesc.GetProperty`
        * :meth:`TypeDesc.CreateArgs`
        * :meth:`TypeDesc.InvokeMethod`


.. method:: TypeDesc.GetInterfaceName()

    Возвращает имя класса (реализуемого интерфейса) как оно описано в библиотеке типов для данного объекта


.. method:: TypeDesc.GetPropertiesNames()

    Возвращает :doc:`коллекцию <Collection>` строк с именами полей класса


.. method:: TypeDesc.HasProperty(PropertyName)

    :PropertyName: **Строка** - имя свойства

    Возвращает булевой значение, говорящее, что у Com-объекта есть поле с указанным именем


.. method:: TypeDesc.GetPropertyType(PropertyName)

    :PropertyName: **Строка** - имя свойства

    Возвращает имя типа, который имеет указанное свойство.
    Возможные типы перечислены `здесь <https://docs.microsoft.com/en-us/windows/win32/api/wtypes/ne-wtypes-varenum>`_ .
    Если указанного свойства у объекта нет, то вернётся пустая строка


.. method:: TypeDesc.SetProperty(PropertyName, Object)

    :PropertyName: **Строка** - название поля COM-объекта
    :Object:       :doc:`./Descriptions/AnyVariant` - устанавливаемое значение

    Задаёт новое значение полю COM-объекта

    .. versionadded:: 5.29.9


.. method:: TypeDesc.GetProperty(PropertyName)

    :PropertyName: **Строка** - название поля COM-объекта

    Получает значение значение поля COM-объекта

    .. versionadded:: 5.29.9


.. method:: TypeDesc.GetMethodsNames()

    Возвращает :doc:`коллекцию <Collection>` строк с именами методов класса

    .. versionadded:: 5.29.9


.. method:: TypeDesc.GetMethodDesc(MethodName)

    :MethodName: **Строка** - имя метода

    Возвращает :doc:`описание интерфейса метода <MethodDesc>` по имени метода

    .. versionadded:: 5.29.9


.. method:: TypeDesc.CreateArgs()

    Создаёт :doc:`набор аргументов <ArgPack>` для последующей передачи в метод

    .. versionadded:: 5.29.9


.. method:: TypeDesc.InvokeMethod(MethodName, Args)

    :MethodName: **Строка** - имя вызываемого метода
    :Args:       :doc:`ArgPack` - набор аргументов

    Вызывает метод по его имени с переданными параметрами и возвращает результат его выполнения, если он есть. Неявного преобразования типов аргументов не происходит

    .. versionadded:: 5.29.9