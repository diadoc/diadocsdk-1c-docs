AddDocument
===========

Метод объекта :doc:`PackageSendTask <PackageSendTask>`

**Синтаксис**


AddDocument(<Type>)


**Параметры**

-  <Type> (строка, обязательный) - название типа документа

Параметр Type может принимать одно из следующих значений:

- Invoice
- InvoiceCorrection
- InvoiceRevision
- InvoiceCorrectionRevision
- XmlAcceptanceCertificate
- XmlTorg12
- UniversalTransferDocument
- UniversalTransferDocumentRevision
- UtdTorg12
- UtdAcceptanceCertificate
- UtdInvoice

**Возвращаемое значение**

Объект документа на отправку, производный от объекта :doc:`DocumentToSend <DocumentToSend>` и 
соответствующий указанному типу:

-  :doc:`InvoiceToSend <InvoiceToSend>` - для типа Invoice

-  :doc:`InvoiceCorrectionToSend <InvoiceCorrectionToSend>` - для типа InvoiceCorrection

-  :doc:`InvoiceRevisionToSend <InvoiceRevisionToSend>` - для типа InvoiceRevision

-  :doc:`InvoiceCorrectionRevisionToSend <InvoiceCorrectionRevisionToSend>` - для типа InvoiceCorrectionRevision

-  :doc:`XmlActToSend <XmlActToSend>` - для типа XmlAcceptanceCertificate

-  :doc:`XmlTorg12ToSend <XmlTorg12ToSend>` - для типа XmlTorg12

-  :doc:`UtdToSend <UtdToSend>` - для типа UniversalTransferDocument



**Описание**


Добавляет новый документ в пакет на отправку.
Метод предназначен для добавления формализованных документов (таких как ТОРГ-12, акт о выполненных работах, 
счет-фактура, исправление счета-фактуры, корректировочный счет-фактура, исправление корректировочного счета-фактуры)
в пакет на отправку.

.. toctree::
   :name: Auto
   :hidden:

   InvoiceToSend <InvoiceToSend>
   InvoiceCorrectionToSend <InvoiceCorrectionToSend>
   InvoiceRevisionToSend <InvoiceRevisionToSend>
   InvoiceCorrectionRevisionToSend <InvoiceCorrectionRevisionToSend>
   XmlActToSend <XmlActToSend>
   XmlTorg12ToSend <XmlTorg12ToSend>
   UtdToSend <UtdToSend>

