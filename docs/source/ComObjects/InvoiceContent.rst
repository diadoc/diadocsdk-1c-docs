InvoiceContent
==============

Представление содержания документа *Счет-фактура* и *Исправление счета-фактуры* в формате приказа `ММВ-7-6/93@ <https://normativ.kontur.ru/document?moduleId=1&documentId=249567>`_.
Является производным объектом от :doc:`BaseContent <BaseContent>`

.. deprecated:: 5.27.0
  Используйте :doc:`DynamicContent`

.. rubric:: Свойства


:Type:
  **Строка, чтение** - тип документа. Константа ``InvoiceContent``

:InvoiceVersion:
  **Строка, чтение/запись** - версия формата счета-фактуры. ``5.01`` или ``5.02``

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
  :doc:`OrganizationInfo <OrganizationInfo>` **, чтение** - данные продавца

:Buyer:
  :doc:`OrganizationInfo <OrganizationInfo>` **, чтение** - данные покупателя

:Shipper:
  :doc:`ShipperOr ConsigneeInfo <ShipperOrConsigneeInfo>` **, чтение** - данные грузоотправителя

:Consignee:
  :doc:`ShipperOr ConsigneeInfo <ShipperOrConsigneeInfo>` **, чтение** - данные грузополучателя

:Signer:
  :doc:`Signer <Signer>` **, чтение** - данные подписанта документа

:Totals:
  :doc:`InvoiceTotals <InvoiceTotals>` **, чтение** - общие итоги по документу

:Items:
  :doc:`Коллекция <Collection>` **объектов** :doc:`InvoiceItem <InvoiceItem>` **, чтение** - табличная часть счета-фактуры

:PaymentDocuments:
  :doc:`Коллекция <Collection>` **объектов** :doc:`PaymentDocument <PaymentDocument>` **, чтение** - список платежно-расчетных документов

:StructedAdditionalInfos:
  :doc:`Коллекция <Collection>` **объектов** :doc:`StructedAdditionalInfo <StructedAdditionalInfo>` **, чтение** - дополнительные сведения



.. rubric:: Методы

+---------------------------+--------------------------------------+---------------------------------------------+
| |InvoiceContent-AddItem|_ | |InvoiceContent-AddPaymentDocument|_ | |InvoiceContent-AddStructedAdditionalInfo|_ |
+---------------------------+--------------------------------------+---------------------------------------------+

.. |InvoiceContent-AddItem| replace:: AddItem()
.. |InvoiceContent-AddPaymentDocument| replace:: AddPaymentDocument()
.. |InvoiceContent-AddStructedAdditionalInfo| replace:: AddStructedAdditionalInfo()



.. _InvoiceContent-AddItem:
.. method:: InvoiceContent.AddItem()

  Добавляет :doc:`новый элемент <InvoiceItem>` в коллекцию *Items* и возвращает его



.. _InvoiceContent-AddPaymentDocument:
.. method:: InvoiceContent.AddPaymentDocument()

  Добавляет :doc:`новый элемент <PaymentDocument>` в коллекцию *PaymentDocuments* и возвращает его



.. _InvoiceContent-AddStructedAdditionalInfo:
.. method:: InvoiceContent.AddStructedAdditionalInfo()

  Добавляет :doc:`новый элемент <StructedAdditionalInfo>` в коллекцию *StructedAdditionalInfos* и возвращает его
