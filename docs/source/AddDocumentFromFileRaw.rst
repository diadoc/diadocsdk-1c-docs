AddDocumentFromFileRaw
======================

Метод объекта :doc:`PackageSendTask <PackageSendTask>`

**Синтаксис**


AddDocumentFromFileRaw(<Type>, <Path>)


**Параметры**

-  <Type> (строка, обязательный) - название типа документа

-  <Path> (строка, обязательный) - путь к файлу с документом


Параметр Type может принимать одно из следующих значений:

- AcceptanceCertificate
- CertificateRegistry
- Contract
- Invoice
- InvoiceCorrection
- InvoiceRevision
- InvoiceCorrectionRevision
- Nonformalized
- NonformalizedProforma
- PriceListAgreement
- ReconciliationAct
- ServiceDetails
- Torg12
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

**Возвращаемое значение**


Объект документа на отправку :doc:`XmlDocumentToSend <XmlDocumentToSend>` производный от объекта :doc:`DocumentToSend <DocumentToSend>`.

**Описание**


Добавляет новый документ в пакет на отправку.
Метод предназначен для добавления формализованных документов (таких как ТОРГ-12, акт о выполненных работах, 
счет-фактура, исправление счета-фактуры, корректировочный счет-фактура, исправление корректировочного счета-фактуры, УПД, иУПД, УКД, иУКД)
и неформализованных документов (таких как акт о выполненных работах, реестр сертификатов, договор, счет на оплату, 
протокол согласования цены, акт сверки, детализация, ТОРГ-12 и других неформализованных документов) в пакет на отправку.
Если добавляеться формализованный документ, то добавляеться исходный файл - "как есть". 



.. toctree::
   :name: Auto
   :hidden:

   XmlDocumentToSend <XmlDocumentToSend>
