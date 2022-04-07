InvoiceCorrectionItem
=====================

`Сведения о товаре (работе, услуге) <https://normativ.kontur.ru/document?moduleId=1&documentId=249567&rangeId=230592>`_

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

:StructedAdditionalInfos:
    :doc:`Коллекция <Collection>` **объектов** :doc:`StructedAdditionalInfo` **, чтение/запись** - дополнительные сведения

    .. versionadded:: 5.0.0


.. rubric:: Методы

.. tabs::

    .. tab:: Все актуальные

        * :meth:`AddStructedAdditionalInfo() <InvoiceCorrectionItem.AddStructedAdditionalInfo>`


.. method:: InvoiceCorrectionItem.AddStructedAdditionalInfo()

    Добавляет :doc:`новый элемент <StructedAdditionalInfo>` в коллекцию **StructedAdditionalInfos** и возвращает его