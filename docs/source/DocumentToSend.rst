Документы на отправку
=====================

Объект DocumentToSend является базовым объектом для всех документов на отправку. Он предназначен для работы с документами, 
входящими в пакет задания на отправку :doc:`PackageSendTask <PackageSendTask>`.


Свойства объекта
----------------


- **Type** (строка, чтение) - тип документа на отправку


Методы
------

- :doc:`AddInitialDocument <AddInitialDocument-(DocumentToSend)>` - добавляет идентификатор
  документа в коллекцию "родительских" документов

- :doc:`AddSubordinateDocument <AddSubordinateDocument-(DocumentToSend)>` - добавляет
  идентификатор документа в коллекцию подчиненных документов

- :doc:`AddInitialDocumentFromPackage <AddInitialDocumentFromPackage>` - добавляет идентификатор
  документа из пакета на отправку в коллекцию "родительских" документов (только для редактируемых пакетов)

- :doc:`AddSubordinateDocumentFromPackage <AddSubordinateDocumentFromPackage>` - добавляет
  идентификатор документа из пакета на отправку в коллекцию подчиненных документов (только для редактируемых пакетов)



Производные объекты 
------------------------------------


Следующие объекты являются производными от DocumentToSend:

.. toctree::
   :name: DocumentToSendChild
   :maxdepth: 1
   :caption: Производные объекты
   :hidden:

   ActToSend <ActToSend> 
   CertificateRegistryToSend <CertificateRegistryToSend>
   ContractToSend <ContractToSend>
   InvoiceToSend <InvoiceToSend>
   InvoiceCorrectionToSend <InvoiceCorrectionToSend>
   InvoiceRevisionToSend <InvoiceRevisionToSend>
   InvoiceCorrectionRevisionToSend <InvoiceCorrectionRevisionToSend>
   NonformalizedDocumentToSend <NonformalizedDocumentToSend>
   PriceListAgreementToSend <PriceListAgreementToSend>
   ProformaInvoiceToSend <ProformaInvoiceToSend>
   ReconciliationActToSend <ReconciliationActToSend>
   ServiceDetailsToSend <ServiceDetailsToSend>
   Torg12ToSend <Torg12ToSend>
   XmlActToSend <XmlActToSend>
   XmlTorg12ToSend <XmlTorg12ToSend>
   UtdToSend <UtdToSend>

-  :doc:`ActToSend <ActToSend>` - акт о выполнении работ в неформализованном виде
-  :doc:`CertificateRegistryToSend <CertificateRegistryToSend>` - реестр сертификатов
-  :doc:`ContractToSend <ContractToSend>` - договор
-  :doc:`InvoiceToSend <InvoiceToSend>` - счет-фактура
-  :doc:`InvoiceCorrectionToSend <InvoiceCorrectionToSend>` - корректировочный счет-фактура
-  :doc:`InvoiceRevisionToSend <InvoiceRevisionToSend>` - исправление счета-фактуры
-  :doc:`InvoiceCorrectionRevisionToSend <InvoiceCorrectionRevisionToSend>` - исправление корректировочного 
   счета-фактуры
-  :doc:`NonformalizedDocumentToSend <NonformalizedDocumentToSend>` - неформализованный документ
-  :doc:`PriceListAgreementToSend <PriceListAgreementToSend>` - протокол согласования цены
-  :doc:`ProformaInvoiceToSend <ProformaInvoiceToSend>` - счет на оплату
-  :doc:`ReconciliationActToSend <ReconciliationActToSend>` - акт сверки
-  :doc:`ServiceDetailsToSend <ServiceDetailsToSend>` - детализация
-  :doc:`Torg12ToSend <Torg12ToSend>` - ТОРГ-12 в неформализованном виде
-  :doc:`XmlActToSend <XmlActToSend>` - акт о выполнении работ в формализованном виде
-  :doc:`XmlTorg12ToSend <XmlTorg12ToSend>` - ТОРГ-12 в формализованном виде
-  :doc:`UtdToSend <UtdToSend>` - универсальный передаточный документ
