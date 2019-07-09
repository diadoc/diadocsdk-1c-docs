InvoiceCorrectionItem
=====================

`Сведения о товаре (работе, услуге) <https://normativ.kontur.ru/document?moduleId=1&documentId=249567&rangeId=230592>`_

.. rubric:: Свойства

:Product:
  **Строка, чтение/запись** - наименование товара

:OriginalValues:
  :doc:`InvoiceItemFields <InvoiceItemFields>` **, чтение** - значения до корректировки

:CorrectedValues:
  :doc:`InvoiceItemFields <InvoiceItemFields>` **, чтение** - значения после корректировки

:AmountsInc:
  :doc:`AmountsDiff <AmountsDiff>` **, чтение** - суммы к увеличению

:AmountsDec:
  :doc:`AmountsDiff <AmountsDiff>` **, чтение** - суммы к уменьшению

:StructedAdditionalInfos:
  :doc:`Коллекция <Collection>` **объектов** :doc:`StructedAdditionalInfo <StructedAdditionalInfo>` **, чтение/запись** - дополнительные сведения



.. rubric:: Методы

+----------------------------------------------------+
| |InvoiceCorrectionItem-AddStructedAdditionalInfo|_ |
+----------------------------------------------------+

.. |InvoiceCorrectionItem-AddStructedAdditionalInfo| replace:: AddStructedAdditionalInfo()


.. _InvoiceCorrectionItem-AddStructedAdditionalInfo:
.. method:: InvoiceCorrectionItem.AddStructedAdditionalInfo()

  Добавляет :doc:`новый элемент <StructedAdditionalInfo>` в коллекцию *StructedAdditionalInfos* и возвращает его
