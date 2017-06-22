UcdSellerContent
================

Объект предназначен для работы с содержанием титула продавца универсального корректировочного документа и является производным объектом от :doc:`BaseContent <BaseContent>`.


Свойства объекта
----------------

- **Function** (строка, чтение/запись, обязательно для заполнения) - функция документа

- **Name** (строка, чтение/запись, строка длиной не более 255 символов) - наименование первичного документа, определенное организацией

- **Date** (дата, чтение/запись, обязательно для запонения) - дата УКД

- **Number** (строка, чтение/запись, обязательно для запонения, строка длиной не более 1000 символов) - номер УКД

- **Invoices** (коллекция :doc:`Collection <Collection>` объектов типа :doc:`InvoiceForCorrectionInfo <InvoiceForCorrectionInfo>`) - счет-фактура (первичный документ), к которому составлен УКД

- **Seller** (объект :doc:`ExtendedOrganizationInfo <ExtendedOrganizationInfo>`, чтение, обязательно для запонения) - данные продавца. В случае УКД с функцией "КСЧФ" и "КСЧФДИС" для продавца должен быть указан адрес

- **Buyer** (объект :doc:`ExtendedOrganizationInfo <ExtendedOrganizationInfo>`, чтение, обязательно для запонения) - данные покупателя. В случае УКД с функцией "КСЧФ" и "КСЧФДИС" для покупателя должен быть указан адрес

- **Signers** (:doc:`коллекция <Collection>` объектов :doc:`ExtendedSigner <ExtendedSigner>`, чтение) - подписанты документа. Для документа должен быть указан по крайней мере один подписант.

- **EventContent** (объект :doc:`EventContent <EventContent>`) - содержание события

- **InvoiceCorrectionTable** (объект :doc:`InvoiceCorrectionTable <InvoiceCorrectionTable>`) - сведения таблицы корректировочного счета-фактуры

- **Currency** (строка, чтение/запись, обязательно для запонения) - код валюты по Общероссийскому классификатору валют

- **CurrencyRate** (строка, чтение/запись) - курс валюты

- **RevisionDate** (дата, чтение/запись) - дата исправления

- **RevisionNumber** (строка, чтение/запись, строка длиной не более 256 символов) - номер исправления

- **AdditionalInfoId** (объект :doc:`AdditionalInfoId <AdditionalInfoId>`, чтение) - информационное поле документа

- **Creator** (строка, чтение/запись, обязательно для запонения, строка длиной не более 1000 символов) - составитель файла обмена счета-фактуры (информации продавца)

- **CreatorBase** (строка, чтение/запись, строка длиной не более 120 символов) - основание, по которому экономический субъект является составителем файла обмена счета-фактуры

- **GovernmentContractInfo** (строка, чтение/запись, строка длиной не более 255 символов) - идентификатор государственного контракта

- **Type** (строка, чтение) - тип документа (возвращает строку "UniversalCorrectionDocument")


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
   
