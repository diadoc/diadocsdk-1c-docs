InvoiceCorrectionTable
======================

`Сведения таблицы корректировочного счета-фактуры (содержание события (факта хозяйственной жизни) 2 - сведения об изменении <https://normativ.kontur.ru/document?moduleId=1&documentId=273231&rangeId=230593>`_

.. deprecated:: 5.27.0
  Используйте :doc:`DynamicContent`


.. rubric:: Свойства

:Items:
  :doc:`Коллекция <Collection>` **объектов** :doc:`ExtendedInvoiceCorrectionItem` **, чтение** - информация о товарах

:TotalsInc:
  :doc:`InvoiceTotalsDiff` **, чтение** - суммы к увеличению

:TotalsDec:
  :doc:`InvoiceTotalsDiff` **, чтение** - суммы к уменьшению



.. rubric:: Методы

+-----------------------------------+
| |InvoiceCorrectionTable-AddItem|_ |
+-----------------------------------+


.. |InvoiceCorrectionTable-AddItem| replace:: AddItem()

.. _InvoiceCorrectionTable-AddItem:
.. method:: InvoiceCorrectionTable.AddItem()

  Добавляет :doc:`новый элементе <ExtendedInvoiceCorrectionItem>` в коллекцию *Items* и возвращает его
