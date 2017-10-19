SendTask
========

Объект предназначен для отправки сообщения на сервер Диадок.

Свойства
--------

-  **Content** (чтение/запись) - содержание документа
-  **CounterAgentId** (строка, чтение/запись) - идентификатор контрагента
-  **FileName** (строка, чтение/запись) - имя файла вложения
-  **Comment** (строка, чтение/запись) - комментарий
-  **OneSDocumentId** (строка, чтение/запись) - идентификатор 1С
-  **OperationId** (строка, чтение/запись) - уникальный идентификатор
   операции. Если отправка документа с заполненным оператором операции завершилась успехам, то все остальные попытки отправки с тем же идентификатором не будут приводить к отправке нового документа, а в результате выполнения метода вернется ссылка на ранее отправленный документ.
-  **CustomDocumentId** (строка, чтение/запись) - внешний идентификатор
-  **FromDepartmentId** (строка, чтение/запись) - идентификатор
   подразделения отправителя
-  **ToDepartmentId** (строка, чтение/запись) - идентификатор подразделения
   получателя
-  **DelaySend** (булево, чтение/запись) признак того, что сообщение будет
   сохранено без отправки
-  **InitialDocuments** (объект :doc:`Collection <Collection>`, чтение) -
   список идентификаторов документов, на которые должен ссылаться
   отправляемый документ
-  **SubordinateDocuments** (объект :doc:`Collection <Collection>`, чтение) -
   список идентификаторов документов, которые должны ссылаться на
   отправляемый
-  **IsInternal** (булево, чтение/запись) - признак того, что сообщение
   является внутренним, то есть сообщением между подразделениями
   организации
-  **ProxyBoxId** (строка, чтение/запись) - идентификатор ящика, промежуточного получателя. Если указан ящик промежуточного получателя, то документа доставится конечному получателя только после того, как промежуточный получатель поставит подпись под документом. Если промежуточный получатель            отклонит документ, то в ящик конечного получателя он не будет доставлен
-  **ProxyDepartmentId** (строка, чтение/запись) -  идентификатор подразделения, в ящике промежуточного получателя
-  **UseShelf** (булево, чтение/запись) - использовать отправку "с полки" (для больших документов)

Свойство **Content** имеет один из следующих типов

-  :doc:`AcceptanceCertificateContent <AcceptanceCertificateContent>` - акт
   о выполнении работ в неформализованном виде
-  :doc:`AcceptanceCertificateSellerContent <AcceptanceCertificateSellerContent>`
   - акт о выполнении работ/оказании услуг, титул исполнителя
-  :doc:`ContractContent <ContractContent>` - договор
-  :doc:`InvoiceContent <InvoiceContent>` - счет-фактура/исправление
   счета-фактуры
-  :doc:`InvoiceCorrectionContent <InvoiceCorrectionContent>` -
   корректировочный счет-фактура/исправление корректировочного
   счета-фактуры
-  :doc:`NonformilizedContent <NonformilizedContent>` -
   неформализованный документ/протокол согласования цены/реестр
   сертификатов/акт сверки/детализация
-  :doc:`ProformaInvoiceContent <ProformaInvoiceContent>` - счет на оплату
-  :doc:`Torg12Content <Torg12Content>` - товарная накладная ТОРГ-12 в
   неформализованном виде
-  :doc:`Torg12SellerContent <Torg12SellerContent>` - товарная накладная
   ТОРГ-12 титул продавца
-  :doc:`UtdSellerContent <UtdSellerContent>` - титул продавца универсального передаточного документа
-  :doc:`UcdSellerContent <UcdSellerContent>` - титул продавца универсального корректировочного документа
-  :doc:`TovTorgSellerContent <TovTorgSellerContent>` - титул продавца торг-12 в формате 551-го приказа
-  :doc:`Act552SellerContent <Act552SellerContent>` - титул продавца акта в формате 552-го приказа

Методы
------

-  :doc:`AddInitialDocument <AddInitialDocument>` - добавляет идентификатор документа в коллекцию "родительских" документов

-  :doc:`AddSubordinateDocument <AddSubordinateDocument>` - добавляет идентификатор документа в коллекцию подчиненных документов

-  :doc:`Send <Send-(SendTask)>` - отправляет документ на сервер

-  :doc:`SendAsync <SendAsync>` - инициирует асинхронную отправку документа

-  :doc:`SaveContent <SaveContent-(SendTask)>` - на основании содержания документа формирует файл документа и сохраняет его на диск

-  :doc:`ValidateContent <ValidateContent-(SendTask)>` - проверяет содержание документа на корректность заполнения

-  :doc:`AddStructuredDataAttachment <AddStructuredDataAttachment>` - добавляет файл со структурированными данными в отправляемый документ

-  :doc:`AddSubordinateOneSDocumentId <AddSubordinateOneSDocumentId-(SendTask)>` - добавляет дополнительный идентификатор 1С для документа

-  :doc:`AddEncryptCertificate <AddEncryptCertificate-(SendTask)>` - добавляет сертификат шифрования документа

.. toctree::
   :name: Auto
   :hidden:

   AddInitialDocument <AddInitialDocument>
   AddSubordinateDocument <AddSubordinateDocument>
   Send <Send-(SendTask)>
   SendAsync <SendAsync>
   SaveContent <SaveContent-(SendTask)>
   ValidateContent <ValidateContent-(SendTask)>
   AddStructuredDataAttachment <AddStructuredDataAttachment>
   AddSubordinateOneSDocumentId <AddSubordinateOneSDocumentId-(SendTask)>
   AddEncryptCertificate <AddEncryptCertificate-(SendTask)>