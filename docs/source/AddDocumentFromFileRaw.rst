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
- UcdInvoiceCorrection
- TovTorg
- XmlAcceptanceCertificate552
- Document
- значения AttachmentVersion Diadoc API

**Возвращаемое значение**

В случае если параметр Type принимает значение Document или одно из значений AttachmentVersion Diadoc API, метод возвращает :doc:`CustomDocumentToSend <CustomDocumentToSend>`. В ином случае метод возвращает объект документа на отправку :doc:`XmlDocumentToSend <XmlDocumentToSend>` производный от объекта :doc:`DocumentToSend <DocumentToSend>`.

**Описание**


Добавляет новый документ в пакет на отправку. Если добавляеться формализованный документ, то добавляеться исходный файл - "как есть". 



.. toctree::
   :name: Auto
   :hidden:

   XmlDocumentToSend <XmlDocumentToSend>
