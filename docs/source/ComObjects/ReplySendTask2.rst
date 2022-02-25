ReplySendTask2
==============

Задание для выполнения ответного действия с документом или с пакетом документов


.. rubric:: Свойства

:ContentItems:
  :doc:`Коллекция <Collection>` **объектов** :doc:`PackageContentItem` **, чтение** - коллекция пар *документ-контент*, для которых создаётся ответное действие

:PowerOfAttorneyToAttach:
  :doc:`PowerOfAttorneyToAttach` **, чтение** - данные об МЧД, которая будет использоваться при подписании

  .. versionadded:: 5.37.0


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
