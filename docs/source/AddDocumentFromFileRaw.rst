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
- UtdTorg12
- UtdAcceptanceCertificate
- UtdInvoice

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

-  :doc:`UtdToSend <UtdToSend>` - для типа UniversalTransferDocument


**Описание**


Добавляет новый документ в пакет на отправку.
Метод предназначен для добавления формализованных документов (таких как ТОРГ-12, акт о выполненных работах, 
счет-фактура, исправление счета-фактуры, корректировочный счет-фактура, исправление корректировочного счета-фактуры)
и неформализованных документов (таких как акт о выполненных работах, реестр сертификатов, договор, счет на оплату, 
протокол согласования цены, акт сверки, детализация, ТОРГ-12 и других неформализованных документов) в пакет на отправку.
Если добавляеться формализованный документ, то добавляеться исходный файл - "как есть". 



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
