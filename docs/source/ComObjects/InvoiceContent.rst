InvoiceContent
==============

Представление содержания документа *Счет-фактура* и *Исправление счета-фактуры* в формате приказа `ММВ-7-6/93@ <https://normativ.kontur.ru/document?moduleId=1&documentId=249567>`_.
Является производным объектом от :doc:`BaseContent`

.. deprecated:: 5.27.0
    Используйте :doc:`DynamicContent`

.. rubric:: Свойства


:Type:
    **Строка, чтение** - тип документа. Константа ``InvoiceContent``

:InvoiceVersion:
    **Строка, чтение/запись** - версия формата счета-фактуры. ``5.01`` или ``5.02``

    .. versionadded:: 4.2.0

:Date:
    **Дата, чтение/запись** - дата счета-фактуры

:Number:
    **Строка, чтение/запись** - номер счета-фактуры

:InvoiceRevisionDate:
    **Дата, чтение/запись** - дата исправленния счета-фактуры

:InvoiceRevisionNumber:
    **Строка, чтение/запись** - номер исправления счета-фактуры

:Currency:
    **Строка, чтение/запись** - код валюты

:Seller:
    :doc:`OrganizationInfo` **, чтение** - данные продавца

:Buyer:
    :doc:`OrganizationInfo` **, чтение** - данные покупателя

:Shipper:
    :doc:`ShipperOrConsigneeInfo` **, чтение** - данные грузоотправителя

:Consignee:
    :doc:`ShipperOrConsigneeInfo` **, чтение** - данные грузополучателя

:Signer:
    :doc:`Signer` **, чтение** - данные подписанта документа

:Totals:
    :doc:`InvoiceTotals` **, чтение** - общие итоги по документу

:Items:
    :doc:`Коллекция <Collection>` **объектов** :doc:`InvoiceItem` **, чтение** - табличная часть счета-фактуры

:PaymentDocuments:
    :doc:`Коллекция <Collection>` **объектов** :doc:`PaymentDocument` **, чтение** - список платежно-расчетных документов

:StructedAdditionalInfos:
    :doc:`Коллекция <Collection>` **объектов** :doc:`StructedAdditionalInfo` **, чтение** - дополнительные сведения

    .. versionadded:: 5.0.0



.. rubric:: Методы

.. tabs::

    .. tab:: Все актуальные
    
        * :meth:`AddItem() <InvoiceContent.AddItem>`
        * :meth:`AddPaymentDocument() <InvoiceContent.AddPaymentDocument>`
        * :meth:`AddStructedAdditionalInfo() <InvoiceContent.AddStructedAdditionalInfo>`

.. method:: InvoiceContent.AddItem()

  Добавляет :doc:`новый элемент <InvoiceItem>` в коллекцию **Items** и возвращает его


.. method:: InvoiceContent.AddPaymentDocument()

    Добавляет :doc:`новый элемент <PaymentDocument>` в коллекцию **PaymentDocuments** и возвращает его


.. method:: InvoiceContent.AddStructedAdditionalInfo()

    Добавляет :doc:`новый элемент <StructedAdditionalInfo>` в коллекцию **StructedAdditionalInfos** и возвращает его