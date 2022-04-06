ExtendedInvoiceCorrectionItem
=============================

`Сведения о товаре (работе, услуге), имущественном праве <https://normativ.kontur.ru/document?moduleId=1&documentId=273231&rangeId=230531>`_


.. deprecated:: 5.27.0
    Используйте :doc:`DynamicContent`


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

.. tabs::

    .. tab:: Все актуальные

        * :meth:`AddStructedAdditionalInfo() <ExtendedInvoiceCorrectionItem.AddStructedAdditionalInfo>`

.. method:: ExtendedInvoiceCorrectionItem.AddStructedAdditionalInfo()

    Добавляет :doc:`новый элемент <StructedAdditionalInfo>` в коллекцию **StructedAdditionalInfos**