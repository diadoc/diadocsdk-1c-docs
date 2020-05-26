PackageSendTask2
================

Задание для отправки документов на сервер Диадок


.. rubric:: Свойства

:CounteragentId:
  **Строка, чтение/запись** - идентификатор получателя. Если получатель совпадает с отправителем, то документ будет отправлен как внутренний

:ToDepartmentId:
  **строка, чтение/запись** - идентификатор подразделения получателя

:FromDepartmentId:
  **строка, чтение/запись** - идентификатор подразделения отправителя

:ProxyBoxId:
  **строка, чтение/запись** - идентификатор промежуточного получателя

:ProxyDepartmentId:
  **строка, чтение/запись** - идентификатор подразделения промежуточного получателя

:IsDraft:
  **булево, чтение/запись** - флаг, показывающий, что данное сообщение является черновиком

:LockDraft:
  **булево, чтение/запись** - флаг, показывающий, что данный черновик является защищенным от изменений

:StrictDraftValidation:
  **булево, чтение/запись** - флаг, включающий проверку правильности черновика

:LockMode:
  **строка, чтение/запись** - режим блокировки сообщения. :doc:`Возможные значения <./Enums/LockMode>`

:DelaySend:
  **булево, чтение/запись** - флаг, показывающий, что документ из сообщения будет помещён в исходящие, но не будет подписан и отправлен сразу

:UseShelf:
  **булево, чтение/запись** - использовать передачу данных небольшими частями (рекомендуется устанавливать для больших документов)

:OperationId:
  **строка, чтение/запись** - уникальный идентификатор операции

:DocumentsToSend:
  :doc:`Коллекция <Collection>` **объектов** :doc:`CustomDocumentToSend` **, чтение** - документы на отправку, добавленные в пакет



.. rubric:: Методы

+----------------------------------+------------------------------------------+--------------------------------------------+
| |PackageSendtTask2-AddDocument|_ | |PackageSendtTask2-AddDocumentFromFile|_ | |PackageSendtTask2-AddDocumentFromBase64|_ |
+----------------------------------+------------------------------------------+--------------------------------------------+
| |PackageSendtTask2-Send|_        | |PackageSendtTask2-SendAsync|_           |                                            |
+----------------------------------+------------------------------------------+--------------------------------------------+


.. |PackageSendtTask2-AddDocument| replace:: AddDocument()
.. |PackageSendtTask2-AddDocumentFromFile| replace:: AddDocumentFromFile()
.. |PackageSendtTask2-AddDocumentFromBase64| replace:: AddDocumentFromBase64()
.. |PackageSendtTask2-Send| replace:: Send()
.. |PackageSendtTask2-SendAsync| replace:: SendAsync()


.. _PackageSendtTask2-AddDocument:
.. method:: PackageSendTask2.AddDocument(TitleName, Function, Version)

  :TitleName: ``строка`` название типа документа
  :Function: ``строка`` функция документа
  :Version: ``строка`` версия документа

  Добавляет :doc:`новый элемент <CustomDocumentToSend>` в коллекцию *DocumentsToSend* и возвращает его



.. _PackageSendtTask2-AddDocumentFromFile:
.. method:: PackageSendTask2.AddDocumentFromFile(TitleName, Function, Version, FilePath)

  :TitleName: ``строка`` название типа документа
  :Function: ``строка`` функция документа
  :Version: ``строка`` версия документа
  :FilePath: ``строка`` путь до файла контрагента

  Добавляет :doc:`новый элемент <CustomDocumentToSend>` в коллекцию *DocumentsToSend*, загружая контент из файла, и возвращает его



.. _PackageSendtTask2-AddDocumentFromBase64:
.. method:: PackageSendTask2.AddDocumentFromBase64(TitleName, Function, Version, Base64)

  :TitleName: ``строка`` название типа документа
  :Function: ``строка`` функция документа
  :Version: ``строка`` версия документа
  :Base64: ``строка`` контент документа в Base64

  Добавляет :doc:`новый элемент <CustomDocumentToSend>` в коллекцию *DocumentsToSend*, загружая контент из Base64 строки, и возвращает его



.. _PackageSendtTask2-Send:
.. method:: PackageSendtTask2.Send()

  Производит отправку документов и возвращает :doc:`отправленные документы <DocumentPackage>`.
  Если отправка пакета с заполненным *OperationId* завершилась успехом, то все остальные попытки отправки с тем же идентификатором не будут приводить к отправке нового пакета, а в результате выполнения метода вернется ранее отправленный пакет



.. _PackageSendtTask2-SendAsync:
.. method:: PackageSendtTask2.SendAsync()

  Асинхронно отправляет пакет документов в Диадок и возвращает :doc:`AsyncResult` с :doc:`отправленными документами <DocumentPackage>` в качестве результата.
  Если отправка пакета с заполненным *OperationId* завершилась успехом, то все остальные попытки отправки с тем же идентификатором не будут приводить к отправке нового пакета, а в результате выполнения метода вернется ранее отправленный пакет




.. seealso:: :doc:`../HowTo/HowTo_post_document`
