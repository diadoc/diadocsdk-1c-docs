TypeDesc
========

Описание COM-объекта


.. rubric:: Методы

+------------------------------+--------------------------------+-----------------------------+--------------------------+-------------------------+
| |TypeDesc-GetInterfaceName|_ | |TypeDesc-GetPropertiesNames|_ | |TypeDesc-GetMethodsNames|_ | |TypeDesc-CreateArgs|_   | |TypeDesc-SetProperty|_ |
+------------------------------+--------------------------------+-----------------------------+--------------------------+-------------------------+
| |TypeDesc-HasProperty|_      | |TypeDesc-GetPropertyType|_    | |TypeDesc-GetMethodDesc|_   | |TypeDesc-InvokeMethod|_ | |TypeDesc-GetProperty|_ |
+------------------------------+--------------------------------+-----------------------------+--------------------------+-------------------------+

.. |TypeDesc-GetInterfaceName| replace:: GetInterfaceName()
.. |TypeDesc-GetPropertiesNames| replace:: GetPropertiesNames()
.. |TypeDesc-HasProperty| replace:: HasProperty()
.. |TypeDesc-GetPropertyType| replace:: GetPropertyType()
.. |TypeDesc-GetMethodsNames| replace:: GetMethodsNames()
.. |TypeDesc-GetMethodDesc| replace:: GetMethodDesc()
.. |TypeDesc-CreateArgs| replace:: CreateArgs()
.. |TypeDesc-InvokeMethod| replace:: InvokeMethod()
.. |TypeDesc-SetProperty| replace:: SetProperty()
.. |TypeDesc-GetProperty| replace:: GetProperty()


.. _TypeDesc-GetInterfaceName:
.. method:: TypeDesc.GetInterfaceName()

Возвращает имя класса (реализуемого интерфейса) как оно описано в библиотеке типов для данного объекта



.. _TypeDesc-GetPropertiesNames:
.. method:: TypeDesc.GetPropertiesNames()

Возвращает :doc:`коллекцию <Collection>` строк с именами полей класса



.. _TypeDesc-HasProperty:
.. method:: TypeDesc.HasProperty(PropertyName)

:PropertyName: ``Регистрозависимая строка`` Имя свойства

Возвращает булевой значение, говорящее, что у Com-объекта есть поле с указанным именем



.. _TypeDesc-GetPropertyType:
.. method:: TypeDesc.GetPropertyType(PropertyName)

:PropertyName: ``Регистрозависимая строка`` Имя свойства

Возвращает имя типа, который имеет указанное свойство.
Возможные типы перечислены `здесь <https://docs.microsoft.com/en-us/windows/win32/api/wtypes/ne-wtypes-varenum>`_ .
Если указанного свойства у объекта нет, то вернётся пустая строка



.. _TypeDesc-GetMethodsNames:
.. method:: TypeDesc.GetMethodsNames()

Возвращает :doc:`коллекцию <Collection>` строк с именами методов класса

.. versionadded:: 5.29.9



.. _TypeDesc-GetMethodDesc:
.. method:: TypeDesc.GetMethodDesc(MethodName)

:MethodName: ``Регистрозависимая строка`` Имя метода

Возвращает :doc:`описание интерфейса метода <MethodDesc>` по имени метода

.. versionadded:: 5.29.9



.. _TypeDesc-CreateArgs:
.. method:: TypeDesc.CreateArgs()

Создаёт :doc:`набор аргументов <ArgPack>` для последующей передачи в метод

.. versionadded:: 5.29.9



.. _TypeDesc-InvokeMethod:
.. method:: TypeDesc.InvokeMethod(MethodName, Args)

:MethodName: ``Регистрозависимая строка`` имя вызываемого метода
:Args:       ``ArgPack`` набор аргументов, представленный объектом :doc:`ArgPack`

Вызывает метод по его имени с переданными параметрами и возвращает результат его выполнения, если он есть. Неявного преобразования типов аргументов не происходит

.. versionadded:: 5.29.9




.. _TypeDesc-SetProperty:
.. method:: TypeDesc.SetProperty(PropertyName, Object)

:PropertyName: ``Регистрозависимая строка`` название поля COM-объекта
:Object:       ``Произвольный объект`` устанавливаемое значение

Задаёт новое значение полю COM-объекта

.. versionadded:: 5.29.9



.. _TypeDesc-GetProperty:
.. method:: TypeDesc.GetProperty(PropertyName)

:PropertyName: ``Регистрозависимая строка`` название поля COM-объекта

Получает значение значение поля COM-объекта

.. versionadded:: 5.29.9
