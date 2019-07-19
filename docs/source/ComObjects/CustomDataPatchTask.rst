CustomDataPatchTask
===================

Задача редактирования коллекции :doc:`Document.CustomData <Document>`


.. rubric:: Свойства

:Items:
  :doc:`Коллекция <Collection>` **объектов** :doc:`CustomDataPatchItem <CustomDataPatchItem>` **, чтение** - коллекция изменений :doc:`Document.CustomData <Document>`


.. rubric:: Методы

+--------------------------------+-----------------------------+----------------------------------+
| |CustomDataPatchTask-AddItem|_ | |CustomDataPatchTask-Send|_ | |CustomDataPatchTask-SendAsync|_ |
+--------------------------------+-----------------------------+----------------------------------+

.. |CustomDataPatchTask-AddItem| replace:: AddItem()
.. |CustomDataPatchTask-Send| replace:: Send()
.. |CustomDataPatchTask-SendAsync| replace:: SendAsync()

.. _CustomDataPatchTask-AddItem:
.. method:: CustomDataPatchTask.AddItem()

  Добавляет :doc:`новый элемент <CustomDataPatchItem>` в коллекцию *Items* и возвращает его


.. _CustomDataPatchTask-Send:
.. method:: CustomDataPatchTask.Send()

  Применяет изменения, описанные в коллекции *Items*


.. _CustomDataPatchTask-SendAsync:
.. method:: CustomDataPatchTask.SendAsync()

  Асинхронно применяет изменения, описанные в коллекции *Items*
