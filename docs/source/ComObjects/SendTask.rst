SendTask
========

.. deprecated:: 5.27.0
    Используйте :doc:`PackageSendTask2 <PackageSendTask2>`

Задание для отправки документа на сервер Диадок


.. rubric:: Свойства

:Content:
  :doc:`BaseContent <BaseContent>` **, чтение** - содержание документа. |SendTask-ContentType|_

:CounterAgentId:
  **Строка, чтение/запись** - идентификатор контрагента

:FileName:
  **Строка, чтение/запись** - имя файла вложения

:Comment:
  **Строка, чтение/запись** - комментарий

:OneSDocumentId:
  **Строка, чтение/запись** - дополнительный идентификатор учётной системы

:OperationId:
  **Строка, чтение/запись** - уникальный идентификатор операции

:CustomDocumentId:
  **Строка, чтение/запись** - внешний идентификатор

:FromDepartmentId:
  **Строка, чтение/запись** - идентификатор подразделения отправителя

  .. versionadded:: 3.0.8

:ToDepartmentId:
  **Строка, чтение/запись** - идентификатор подразделения получателя
  
  .. versionadded:: 3.0.8

:DelaySend:
  **Строка, чтение/запись** - признак того, что сообщение будет отправлено в Диадок без доставки до контрагента

:InitialDocuments:
  :doc:`Коллекция <Collection>` **строк, чтение** - список идентификаторов документов, на которые должен ссылаться отправляемый документ как на родительские

:SubordinateDocuments:
  :doc:`Коллекция <Collection>` **строк, чтение** - список идентификаторов документов, на которые должны ссылаться на отправляемый документ как на подчинённые

:IsInternal:
  **Булево, чтение/запись** - признак того, что сообщение является внутренним, то есть сообщением между подразделениями организации

  .. versionadded:: 3.0.8

:ProxyBoxId:
  **Строка, чтение/запись** - идентификатор ящика, промежуточного получателя

:ProxyDepartmentId:
  **Строка, чтение/запись** -  идентификатор подразделения, в ящике промежуточного получателя

:UseShelf:
  **Булево, чтение/запись** - использовать отправку "с полки" (для больших документов)

:SaveContentPath:
  **Строка, чтение** - путь к папке, для сохранения сгенерированного содержимого


.. rubric:: Методы

+------------------------------------------+------------------------------------+-----------------------------------------+
| |SendTask-AddInitialDocument|_           | |SendTask-AddSubordinateDocument|_ | |SendTask-Send|_                        |
+------------------------------------------+------------------------------------+-----------------------------------------+
| |SendTask-SendAsync|_                    | |SendTask-SaveContent|_            | |SendTask-AddStructuredDataAttachment|_ |
+------------------------------------------+------------------------------------+-----------------------------------------+
| |SendTask-AddSubordinateOneSDocumentId|_ | |SendTask-AddEncryptCertificate|_  |                                         |
+------------------------------------------+------------------------------------+-----------------------------------------+

.. |SendTask-AddInitialDocument| replace:: AddInitialDocument()
.. |SendTask-AddSubordinateDocument| replace:: AddSubordinateDocument()
.. |SendTask-Send| replace:: Send()
.. |SendTask-SendAsync| replace:: SendAsync()
.. |SendTask-SaveContent| replace:: SaveContent()
.. |SendTask-AddStructuredDataAttachment| replace:: AddStructuredDataAttachment()
.. |SendTask-AddSubordinateOneSDocumentId| replace:: AddSubordinateOneSDocumentId()
.. |SendTask-AddEncryptCertificate| replace:: AddEncryptCertificate()



.. _SendTask-AddInitialDocument:
.. method:: SendTask.AddInitialDocument(DocumentId)

  :DocumentId: ``строка`` идентификатор документа в Диадок

  Добавляет новый элемент в коллекцию *InitialDocuments*



.. _SendTask-AddSubordinateDocument:
.. method:: SendTask.AddSubordinateDocument(DocumentId)

  :DocumentId: ``строка`` идентификатор документа в Диадок

  Добавляет новый элемент в коллекцию *SubordinateDocuments*



.. _SendTask-Send:
.. method:: SendTask.Send()

  Отправляет документ на сервер и возвращает :doc:`отправленный документ <Document>`



.. _SendTask-SendAsync:
.. method:: SendTask.SendAsync()

  Асинхронно отправляет документ на сервер и возвращает :doc:`AsyncResult` с :doc:`Document` в качестве результата



.. _SendTask-SaveContent:
.. method:: SendTAsk.SaveContent(FilePath)

  :FilePath: ``строка`` путь до файла, в который будет записан контент

  Формирует файл документа и сохраняет результат на диск



.. _SendTask-AddStructuredDataAttachment:
.. method:: SendTask.AddStructuredDataAttachment(FileName, FilePath)

  :FileName: ``строка`` имя файла, с которым будут отправлены структурированные данные
  :FilePath: ``строка`` путь до файл со структурированными данными

  Добавляет файл со структурированными данными в отправляемый документ

  .. deprecated:: 5.19.1
    Используйте :doc:`CustomDataPatchTask`



.. _SendTask-AddSubordinateOneSDocumentId:
.. method:: SendTask.AddSubordinateOneSDocumentId(OneSId)

  :OneSId: ``строка`` идентификатор учётной системы

  Добавляет дополнительный документ с укзанным идентификатором как подчинённый к отправляемому документу



.. _SendTask-AddEncryptCertificate:
.. method:: SendTask.AddEncryptCertificate(Certificate)

  :Certificate: :doc:`PersonalCertificate` сертификат КЭП

  Добавляет сертификат для шифрования документа




.. rubric:: Дополнительная информация

.. |SendTask-ContentType| replace:: возможные типы контента
.. _SendTask-ContentType:

========================================= ================================================================================================
Тип *Content*                             Описание
========================================= ================================================================================================
:doc:`AcceptanceCertificateContent`       акт о выполнении работ в неформализованном виде
:doc:`AcceptanceCertificateSellerContent` акт о выполнении работ/оказании услуг, титул исполнителя
:doc:`ContractContent`                    договор
:doc:`InvoiceContent`                     счет-фактура/исправление счета-фактуры
:doc:`InvoiceCorrectionContent`           корректировочный счет-фактура/исправление корректировочного счета-фактуры
:doc:`NonformalizedContent`               неформализованный документ/протокол согласования цены/реестр сертификатов/акт сверки/детализация
:doc:`NonformalizedProformaContent`       счет на оплату
:doc:`Torg12Content`                      товарная накладная ТОРГ-12 в неформализованном виде
:doc:`Torg12SellerContent`                товарная накладная ТОРГ-12 титул продавца
:doc:`UtdSellerContent`                   титул продавца универсального передаточного документа
:doc:`UcdSellerContent`                   титул продавца универсального корректировочного документа
:doc:`TovTorgSellerContent`               титул продавца торг-12 в формате 551-го приказа
:doc:`Act552SellerContent`                титул продавца акта в формате 552-го приказа
========================================= ================================================================================================


.. seealso:: :doc:`../HowTo/HowTo_post_document`
