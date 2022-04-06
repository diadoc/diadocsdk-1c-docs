ArgPack
=======

Набор аргументов функции COM-объекта

.. versionadded:: 5.29.9


.. rubric:: Свойства

:Args:
    :doc:`Коллекция <Collection>` **объектов** :doc:`произвольного типа, <Descriptions/AnyVariant>` **чтение** - набор аргументов


.. rubric:: Методы

.. tabs::

    .. tab:: Все актуальные

        * :meth:`Add() <ArgPack.Add>`

        * :meth:`Set() <ArgPack.Set>`

.. method:: ArgPack.Add(Object)

    :Object: :doc:`Descriptions/AnyVariant` - аргумент функции

    Добавляет новый аргумент в коллекцию аргументов


.. method:: ArgPack.Set(Object)

    :Object: :doc:`Descriptions/AnyVariant` - аргумент функции

    Добавляет новый аргумент в коллекцию аргументов и возвращает обновлённый объект :doc:`ArgPack`