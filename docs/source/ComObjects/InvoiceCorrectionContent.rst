InvoiceCorrectionContent
========================

Представление содержания документа *Корректировочный счет-фактура* и *Исправление корректировочного счета-фактуры* в формате `ММВ-7-6/93@ <https://normativ.kontur.ru/document?moduleId=1&documentId=249567&rangeId=230580>`_.
Является производным объектом от :doc:`BaseContent <BaseContent>`


.. rubric:: Свойства

:Type:
  **Строка, чтение** - тип документа. Константа ``InvoiceCorrectionContent``

:InvoiceVersion:
  **Строка, чтение/запись** - версия формата счета-фактуры. ``5.01`` или ``5.02``

:OriginalInvoices:
  :doc:`Коллекция <Collection>` **объектов** :doc:`OriginalInvoice <OriginalInvoice>` **, чтение** - данные об счет-фактурах, на основании которых был выставлен корректировочный счет-фактура

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
  :doc:`OrganizationInfo <OrganizationInfo>` **, чтение** - данные продавца

:Buyer:
  :doc:`OrganizationInfo <OrganizationInfo>` **, чтение** - данные покупателя

:Signer:
  :doc:`Signer <Signer>` **, чтение** - данные подписанта документа

:Items:
  :doc:`Коллекция <Collection>` **объектов** :doc:`InvoiceCorrectionItem <InvoiceCorrectionItem>` **, чтение** - табличная часть корректировочного счета-фактуры

:TotalsInc:
  :doc:`InvoiceTotalsDiff <InvoiceTotalsDiff>` **, чтение** - итоговая сумма к увеличению

:TotalsDec:
  :doc:`InvoiceTotalsDiff <InvoiceTotalsDiff>` **, чтение** - итоговая сумма к уменьшению

:StructedAdditionalInfos:
  :doc:`Коллекция <Collection>` **объектов** :doc:`StructedAdditionalInfo <StructedAdditionalInfo>` **, чтение** - дополнительные сведения



.. rubric:: Методы

+-------------------------------------+------------------------------------------------+-------------------------------------------------------+
| |InvoiceCorrectionContent-AddItem|_ | |InvoiceCorrectionContent-AddOriginalInvoice|_ | |InvoiceCorrectionContent-AddStructedAdditionalInfo|_ |
+-------------------------------------+------------------------------------------------+-------------------------------------------------------+

.. |InvoiceCorrectionContent-AddItem| replace:: AddItem()
.. |InvoiceCorrectionContent-AddOriginalInvoice| replace:: AddOriginalInvoice()
.. |InvoiceCorrectionContent-AddStructedAdditionalInfo| replace:: AddStructedAdditionalInfo()



.. _InvoiceCorrectionContent-AddItem:
.. method:: InvoiceCorrectionContent.AddItem()

  Добавляет :doc:`новый элемент <InvoiceItem>` в коллекцию *Items* и возвращает его



.. _InvoiceCorrectionContent-AddOriginalInvoice:
.. method:: InvoiceCorrectionContent.AddPaymentDocument()

  Добавляет :doc:`новый элемент <OriginalInvoice>` в коллекцию *OriginalInvoices* и возвращает его



.. _InvoiceCorrectionContent-AddStructedAdditionalInfo:
.. method:: InvoiceCorrectionContent.AddStructedAdditionalInfo()

  Добавляет :doc:`новый элемент <StructedAdditionalInfo>` в коллекцию *StructedAdditionalInfos* и возвращает его
