UcdSellerContent
================

Объект предназначен для работы с содержанием формализованного документа "Универсальный передаточный документа" в формате приказа `ММВ-7-15/189@ <https://normativ.kontur.ru/document?moduleId=1&documentId=273231>`_ и является производным объектом от :doc:`BaseContent <BaseContent>`.

Свойства объекта
----------------

- **Type** (строка, чтение) - тип документа (возвращает строку "UniversalCorrectionDocument")

- **Function** (строка, чтение/запись) - функция документа

- **Name** (строка, чтение/запись) - наименование первичного документа, определенное организацией

- **Date** (дата, чтение/запись) - дата УКД

- **Number** (строка, чтение/запись) - номер УКД

- **Invoices** (:doc:`коллекция <Collection>` объектов :doc:`InvoiceForCorrectionInfo <InvoiceForCorrectionInfo>`) - счет-фактура (первичный документ), к которому составлен УКД

- **Seller** (:doc:`ExtendedOrganizationInfo <ExtendedOrganizationInfo>`, чтение) - данные продавца. В случае УКД с функцией "КСЧФ" и "КСЧФДИС" для продавца должен быть указан адрес

- **Buyer** (:doc:`ExtendedOrganizationInfo <ExtendedOrganizationInfo>`, чтение) - данные покупателя. В случае УКД с функцией "КСЧФ" и "КСЧФДИС" для покупателя должен быть указан адрес

- **Signers** (:doc:`коллекция <Collection>` объектов :doc:`ExtendedSigner <ExtendedSigner>`, чтение) - подписанты документа. Для документа должен быть указан по крайней мере один подписант.

- **EventContent** (:doc:`EventContent <EventContent>`) - содержание события

- **InvoiceCorrectionTable** (:doc:`InvoiceCorrectionTable <InvoiceCorrectionTable>`) - сведения таблицы корректировочного счета-фактуры

- **Currency** (строка, чтение/запись) - код валюты по Общероссийскому классификатору валют

- **CurrencyRate** (строка, чтение/запись) - курс валюты

- **RevisionDate** (дата, чтение/запись) - дата исправления

- **RevisionNumber** (строка, чтение/запись) - номер исправления

- **AdditionalInfoId** (:doc:`AdditionalInfoId <AdditionalInfoId>`, чтение) - информационное поле документа

- **Creator** (строка, чтение/запись) - составитель файла обмена счета-фактуры (информации продавца)

- **CreatorBase** (строка, чтение/запись) - основание, по которому экономический субъект является составителем файла обмена счета-фактуры

- **GovernmentContractInfo** (строка, чтение/запись) - идентификатор государственного контракта


Свойство **Function** принимает одно из следующих значений:
 
-  "Invoice" - КСЧФ
-  "Basic" - ДИС
-  "InvoiceAndBasic" - КСЧФДИС


Методы объекта
--------------

-  :doc:`AddSigner <AddSigner-(UcdSellerContent)>` - добавляет подписанта

-  :doc:`AddInvoice <AddInvoice-(UcdSellerContent)>` - добавляет счет-фактуру (первичный документ), к которому составлен УКД


.. toctree::
   :name: Auto
   :hidden:

   AddSigner <AddSigner-(UcdSellerContent)>
   AddInvoice <AddInvoice-(UcdSellerContent)>
   InvoiceForCorrectionInfo <InvoiceForCorrectionInfo>
   EventContent <EventContent>
   InvoiceCorrectionTable <InvoiceCorrectionTable>
   
