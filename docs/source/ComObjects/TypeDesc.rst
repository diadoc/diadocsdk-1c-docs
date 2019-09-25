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

Возвращает строковое имя интерфейса, который реализует класс



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

Возвращает строкое имя типа, которое имеет указанное свойство. Если указанного свойства у объекта нет, то вернётся пустая строка
