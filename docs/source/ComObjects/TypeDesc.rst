TypeDesc
========

Описание COM-объекта


.. rubric:: Методы

+------------------------------+--------------------------------+
| |TypeDesc-GetInterfaceName|_ | |TypeDesc-GetPropertiesNames|_ |
+------------------------------+--------------------------------+
| |TypeDesc-HasProperty|_      | |TypeDesc-GetPropertyType|_    |
+------------------------------+--------------------------------+

.. |TypeDesc-GetInterfaceName| replace:: GetInterfaceName()
.. |TypeDesc-GetPropertiesNames| replace:: GetPropertiesNames()
.. |TypeDesc-HasProperty| replace:: HasProperty()
.. |TypeDesc-GetPropertyType| replace:: GetPropertyType()


.. _TypeDesc-GetInterfaceName:
.. method:: TypeDesc.GetInterfaceName()

Возвращает имя класса (реализуемого интерфейса) как оно описано в библиотеке типов для данного объекта



.. _TypeDesc-GetPropertiesNames:
.. method:: TypeDesc.GetPropertiesNames()

Возвращает `коллекцию <Collection>` строк с именами полей класса



.. _TypeDesc-HasProperty:
.. method:: TypeDesc.HasProperty(PropertyName)

:PropertyName: ``Регистрозависимая строка`` Имя свойства

Возвращает булевой значение, говорящее, что у Com-объекта есть поле с указанным именем



.. _TypeDesc-GetPropertyType:
.. method:: TypeDesc.GetPropertyType(PropertyName)

:PropertyName: ``Регистрозависимая строка`` Имя свойства

Возвращает строковое имя типа, которое имеет указанное свойство.
Возможные типы перечислены `здесь <https://docs.microsoft.com/en-us/windows/win32/api/wtypes/ne-wtypes-varenum>`_
Если указанного свойства у объекта нет, то вернётся пустая строка
