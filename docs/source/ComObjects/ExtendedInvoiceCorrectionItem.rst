ExtendedInvoiceCorrectionItem
=============================

`Сведения о товаре (работе, услуге), имущественном праве <https://normativ.kontur.ru/document?moduleId=1&documentId=273231&rangeId=230531>`_


.. rubric:: Свойства

:Product:
  **Строка, чтение/запись** - наименование товара

:OriginalValues:
  :doc:`InvoiceItemFields` **, чтение** - значения до корректировки

:CorrectedValues:
  :doc:`InvoiceItemFields` **, чтение** - значения после корректировки

:AmountsInc:
  :doc:`AmountsDiff` **, чтение** - суммы к увеличению

:AmountsDec:
  :doc:`AmountsDiff` **, чтение** - суммы к уменьшению

:ItemAccountDebit:
  **Строка, чтение/запись** - корреспондирующие счета: дебет

:ItemAccountCredit:
  **Строка, чтение/запись** - корреспондирующие счета: кредит

:StructedAdditionalInfos:
  :doc:`Коллекция <Collection>` **объектов** :doc:`StructedAdditionalInfo` **, чтение** - дополнительные сведения



.. rubric:: Методы

+------------------------------------------------------------+
| |ExtendedInvoiceCorrectionItem-AddStructedAdditionalInfo|_ |
+------------------------------------------------------------+

.. |ExtendedInvoiceCorrectionItem-AddStructedAdditionalInfo| replace:: AddStructedAdditionalInfo()



.. _ExtendedInvoiceCorrectionItem-AddStructedAdditionalInfo:
.. method:: ExtendedInvoiceCorrectionItem.AddStructedAdditionalInfo()

    Добавляет :doc:`новый элемент <StructedAdditionalInfo>` в коллекцию *StructedAdditionalInfos*
