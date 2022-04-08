InvoiceCorrectionContent
========================

Представление содержания документа *Корректировочный счет-фактура* и *Исправление корректировочного счета-фактуры* в формате `ММВ-7-6/93@ <https://normativ.kontur.ru/document?moduleId=1&documentId=249567&rangeId=230580>`_.
Является производным объектом от :doc:`BaseContent`

.. deprecated:: 5.27.0
    Используйте :doc:`DynamicContent`


.. rubric:: Свойства

:Type:
    **Строка, чтение** - тип документа. Константа ``InvoiceCorrectionContent``

:InvoiceVersion:
    **Строка, чтение/запись** - версия формата счета-фактуры. ``5.01`` или ``5.02``

    .. versionadded:: 4.2.0

:OriginalInvoices:
    :doc:`Коллекция <Collection>` **объектов** :doc:`OriginalInvoice` **, чтение** - данные об счет-фактурах, на основании которых был выставлен корректировочный счет-фактура

    .. versionadded:: 5.0.0

:InvoiceCorrectionDate:
    **Дата, чтение/запись** - дата КСФ

:InvoiceCorrectionNumber:
    **Строка, чтение/запись** - номер КСФ

:InvoiceCorrectionRevisionDate:
    **Дата, чтение/запись** - дата исправления КСФ

:InvoiceCorrectionRevisionNumber:
    **Строка, чтение/запись** - номер исправления КСФ

:Currency:
    **Строка, чтение/запись** - код валюты

:Seller:
    :doc:`OrganizationInfo` **, чтение** - данные продавца

:Buyer:
    :doc:`OrganizationInfo` **, чтение** - данные покупателя

:Signer:
    :doc:`Signer` **, чтение** - данные подписанта документа

:Items:
    :doc:`Коллекция <Collection>` **объектов** :doc:`InvoiceCorrectionItem` **, чтение** - табличная часть корректировочного счета-фактуры

:TotalsInc:
    :doc:`InvoiceTotalsDiff` **, чтение** - итоговая сумма к увеличению

:TotalsDec:
    :doc:`InvoiceTotalsDiff` **, чтение** - итоговая сумма к уменьшению

:StructedAdditionalInfos:
    :doc:`Коллекция <Collection>` **объектов** :doc:`StructedAdditionalInfo` **, чтение** - дополнительные сведения

    .. versionadded:: 5.0.0



.. rubric:: Методы

.. tabs::

    .. tab:: Все актуальные

        * :meth:`AddItem() <InvoiceCorrectionContent.AddItem>`
        * :meth:`AddOriginalInvoice() <InvoiceCorrectionContent.AddOriginalInvoice>`
        * :meth:`AddStructedAdditionalInfo() <InvoiceCorrectionContent.AddStructedAdditionalInfo>`


.. method:: InvoiceCorrectionContent.AddItem()

    Добавляет :doc:`новый элемент <InvoiceItem>` в коллекцию **Items** и возвращает его


.. method:: InvoiceCorrectionContent.AddOriginalInvoice()

    Добавляет :doc:`новый элемент <OriginalInvoice>` в коллекцию **OriginalInvoices** и возвращает его


.. method:: InvoiceCorrectionContent.AddStructedAdditionalInfo()

    Добавляет :doc:`новый элемент <StructedAdditionalInfo>` в коллекцию **StructedAdditionalInfos** и возвращает его