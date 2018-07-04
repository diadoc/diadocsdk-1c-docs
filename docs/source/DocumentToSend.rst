Документы на отправку
=====================

Объект вляется базовым объектом для всех документов на отправку. Он предназначен для работы с документами, входящими в пакет задания на отправку :doc:`PackageSendTask <PackageSendTask>`

Свойства объекта
----------------

- **Type** (строка, чтение) - тип документа на отправку

- **NeedReceipt** (булево, чтение/запись) - флаг принудительного запроса извещения о получении по документу. Если установлено ложное значение, то ИоП запрашивает только по документам, чей документооборот это предполагает (Счета-фактуры и УПД с фактурной частью)

Методы
------

- :doc:`AddInitialDocument <AddInitialDocument-(DocumentToSend)>` - добавляет идентификатор документа в коллекцию "родительских" документов

- :doc:`AddSubordinateDocument <AddSubordinateDocument-(DocumentToSend)>` - добавляет идентификатор документа в коллекцию подчиненных документов

- :doc:`AddInitialDocumentFromPackage <AddInitialDocumentFromPackage>` - добавляет идентификатор документа из пакета на отправку в коллекцию "родительских" документов (только для редактируемых пакетов)

- :doc:`AddSubordinateDocumentFromPackage <AddSubordinateDocumentFromPackage>` - добавляет идентификатор документа из пакета на отправку в коллекцию подчиненных документов (только для редактируемых пакетов)

Производные объекты 
-------------------

Следующие объекты являются производными от DocumentToSend:

-  :doc:`ActToSend <ActToSend>` - Акт о выполнении работ в неформализованном виде
-  :doc:`CertificateRegistryToSend <CertificateRegistryToSend>` - Реестр сертификатов
-  :doc:`ContractToSend <ContractToSend>` - Договор
-  :doc:`InvoiceToSend <InvoiceToSend>` - Счет-фактура в формате приказа ММВ-7-6/93@
-  :doc:`InvoiceCorrectionToSend <InvoiceCorrectionToSend>` - Корректировочный счет-фактура
-  :doc:`InvoiceRevisionToSend <InvoiceRevisionToSend>` - Исправление счета-фактуры в формате приказа ММВ-7-6/93@
-  :doc:`InvoiceCorrectionRevisionToSend <InvoiceCorrectionRevisionToSend>` - Исправление корректировочного счета-фактуры
-  :doc:`NonformalizedDocumentToSend <NonformalizedDocumentToSend>` - Неформализованный документ
-  :doc:`PriceListAgreementToSend <PriceListAgreementToSend>` - Протокол согласования цены
-  :doc:`ProformaInvoiceToSend <ProformaInvoiceToSend>` - Счет на оплату
-  :doc:`ReconciliationActToSend <ReconciliationActToSend>` - Акт сверки
-  :doc:`ServiceDetailsToSend <ServiceDetailsToSend>` - Детализация
-  :doc:`Torg12ToSend <Torg12ToSend>` - ТОРГ-12 в неформализованном виде
-  :doc:`XmlActToSend <XmlActToSend>` - Акт о выполнении работ в формате приказа ММВ-7-6/172@
-  :doc:`XmlTorg12ToSend <XmlTorg12ToSend>` - ТОРГ-12 в формате приказа ММВ-7-6/172@
-  :doc:`UtdToSend <UtdToSend>` - Универсальный передаточный документ
-  :doc:`UcdToSend <UcdToSend>` - Универсальный корректировочный документ
-  :doc:`TovTorgToSend <TovTorgToSend>` - ТОРГ-12 в формате приказа ММВ-7-10/551@
-  :doc:`XmlAct552ToSend <XmlAct552ToSend>` - Акт в формате приказа ММВ-7-10/552@
-  :doc:`CustomDocumentToSend <CustomDocumentToSend>` - документ произвольного типа