ReplySendTask2
==============

Задание для выполнения ответного действия с документом или с пакетом документов


.. rubric:: Свойства

:ContentItems:
  :doc:`Коллекция <Collection>` **объектов** :doc:`PackageContentItem` **, чтение** - коллекция пар *документ-контент*, для которых создаётся ответное действие


.. rubric:: Методы

+------------------------+-----------------------------+
| |ReplySendTask2-Send|_ | |ReplySendTask2-SendAsync|_ |
+------------------------+-----------------------------+


.. |ReplySendTask2-Send| replace:: Send()
.. |ReplySendTask2-SendAsync| replace:: SendAsync()


.. _ReplySendTask2-Send:
.. method:: ReplySendTask2.Send()

  Применяет ответные действия



.. _ReplySendTask2-SendAsync:
.. method:: ReplySendTask2.SendAsync()

  Применяет ответные действия асинхронно. Возвращает :doc:`AsyncResult` с булевым типом результата
