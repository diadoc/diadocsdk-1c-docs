AddDocumentFromFile
===================

Метод объекта :doc:`PackageSendTask <PackageSendTask>`

**Синтаксис**


AddDocumentFromFile(<Type>, <Path>)


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
- TovTorg
- XmlAcceptanceCertificate552
- Document
- значения AttachmentVersion Diadoc API (поддерживаются: utd_05_01_01, utd_05_01_02, utd_05_01_04, utd_05_01_05, ucd_05_01_01, ucd_05_01_02, ucd_05_01_03, rezru_05_01_01, rezru_05_01_02, tovtorg_05_01_02, tovtorg_05_01_04, act_05_01_01, act_05_01_02, invoice_05_01_01, invoice_05_01_03, invoice_05_02_01, invoice_05_02_02, invoicecor_05_01_03, invoicecor_05_02_01, invoicecor_05_02_02, torg12_05_01_01, torg12_05_01_02)

**Возвращаемое значение**


Объект документа на отправку, производный от объекта :doc:`DocumentToSend <DocumentToSend>` и 
соответствующий указанному типу:

-  :doc:`ActToSend <ActToSend>` - для типа AcceptanceCertificate

-  :doc:`CertificateRegistryToSend <CertificateRegistryToSend>` - для типа CertificateRegistry

-  :doc:`ContractToSend <ContractToSend>` - для типа Contract

-  :doc:`InvoiceToSend <InvoiceToSend>` - для типа Invoice

-  :doc:`InvoiceCorrectionToSend <InvoiceCorrectionToSend>` - для типа InvoiceCorrection

-  :doc:`InvoiceRevisionToSend <InvoiceRevisionToSend>` - для типа InvoiceRevision

-  :doc:`InvoiceCorrectionRevisionToSend <InvoiceCorrectionRevisionToSend>` - для типа InvoiceCorrectionRevision

-  :doc:`NonformalizedDocumentToSend <NonformalizedDocumentToSend>` - для типа Nonformalized

-  :doc:`ProformaInvoiceToSend <ProformaInvoiceToSend>` - для типа NonformalizedProforma

-  :doc:`PriceListAgreementToSend <PriceListAgreementToSend>` - для типа PriceListAgreement

-  :doc:`ReconciliationActToSend <ReconciliationActToSend>` - для типа ReconciliationAct

-  :doc:`ServiceDetailsToSend <ServiceDetailsToSend>` - для типа ServiceDetails

-  :doc:`Torg12ToSend <Torg12ToSend>` - для типа Torg12

-  :doc:`XmlActToSend <XmlActToSend>` - для типа XmlAcceptanceCertificate

-  :doc:`XmlTorg12ToSend <XmlTorg12ToSend>` - для типа XmlTorg12

-  :doc:`UtdToSend <UtdToSend>` - для типа UniversalTransferDocument, UniversalTransferDocumentRevision, UtdInvoice, UtdAcceptanceCertificate и UtdTorg12

-  :doc:`UcdToSend <UcdToSend>` - для типа UniversalCorrectionDocument, UniversalCorrectionDocumentRevision, UcdInvoiceCorrection

-  :doc:`TovTorgToSend <TovTorgToSend>` - для типа TovTorg

-  :doc:`XmlAct552ToSend <XmlAct552ToSend>` - для типа XmlAcceptanceCertificate552

-  :doc:`CustomDocumentToSend <CustomDocumentToSend>` - для типа Document или для значений AttachmentVersion Diadoc API

**Описание**

Добавляет новый документ в пакет на отправку.

.. toctree::
   :name: Auto
   :hidden:

   ActToSend <ActToSend>
   CertificateRegistryToSend <CertificateRegistryToSend>
   ContractToSend <ContractToSend>
   InvoiceToSend <InvoiceToSend>
   InvoiceCorrectionToSend <InvoiceCorrectionToSend>
   InvoiceRevisionToSend <InvoiceRevisionToSend>
   InvoiceCorrectionRevisionToSend <InvoiceCorrectionRevisionToSend>
   NonformalizedDocumentToSend <NonformalizedDocumentToSend>
   ProformaInvoiceToSend <ProformaInvoiceToSend>
   PriceListAgreementToSend <PriceListAgreementToSend>
   ReconciliationActToSend <ReconciliationActToSend>
   ServiceDetailsToSend <ServiceDetailsToSend>
   Torg12ToSend <Torg12ToSend>
   XmlActToSend <XmlActToSend>
   XmlTorg12ToSend <XmlTorg12ToSend>
   UtdToSend <UtdToSend>
   CustomDocumentToSend <CustomDocumentToSend>
