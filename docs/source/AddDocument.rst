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
- UniversalCorrectionDocument
- UniversalCorrectionDocumentRevision
- UtdTorg12
- UtdAcceptanceCertificate
- UtdInvoice
- UcdInvoiceCorrection
- TovTorg
- XmlAcceptanceCertificate552
- значения AttachmentVersion Diadoc API (поддерживаются: utd_05_01_01, utd_05_01_02, ucd_05_01_01, rezru_05_01_01, tovtorg_05_01_02, act_05_01_01, act_05_01_02, invoice_05_01_01, invoice_05_01_03, invoice_05_02_01, invoicecor_05_01_03, invoicecor_05_02_01, torg12_05_01_01, torg12_05_01_02)

**Возвращаемое значение**

Объект документа на отправку, производный от объекта :doc:`DocumentToSend <DocumentToSend>` и 
соответствующий указанному типу:

-  :doc:`InvoiceToSend <InvoiceToSend>` - для типа Invoice

-  :doc:`InvoiceCorrectionToSend <InvoiceCorrectionToSend>` - для типа InvoiceCorrection

-  :doc:`InvoiceRevisionToSend <InvoiceRevisionToSend>` - для типа InvoiceRevision

-  :doc:`InvoiceCorrectionRevisionToSend <InvoiceCorrectionRevisionToSend>` - для типа InvoiceCorrectionRevision

-  :doc:`XmlActToSend <XmlActToSend>` - для типа XmlAcceptanceCertificate

-  :doc:`XmlTorg12ToSend <XmlTorg12ToSend>` - для типа XmlTorg12

-  :doc:`UtdToSend <UtdToSend>` - для типа UniversalTransferDocument, UniversalTransferDocumentRevision, UtdInvoice, UtdAcceptanceCertificate и UtdTorg12

-  :doc:`UcdToSend <UcdToSend>` - для типа UniversalCorrectionDocument, UniversalCorrectionDocumentRevision, UcdInvoiceCorrection

-  :doc:`TovTorgToSend <TovTorgToSend>` - для типа TovTorg

-  :doc:`XmlAct552ToSend <XmlAct552ToSend>` - для типа XmlAcceptanceCertificate552

-  :doc:`CustomDocumentToSend <CustomDocumentToSend>` - "любой документ" на отправку 

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
   UcdToSend <UcdToSend>
   TovTorgToSend <TovTorgToSend>
   XmlAct552ToSend <XmlAct552ToSend>
   CustomDocumentToSend <CustomDocumentToSend>

