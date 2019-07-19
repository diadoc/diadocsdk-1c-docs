CustomDocumentToSend
====================

Документ на отправку произвольного типа.
Является производным объектом от :doc:`DocumentToSend <DocumentToSend>`


.. rubric:: Свойства

:Type:
  **Строка, чтение** - тип документа. Константа ``Document``

:FileName:
  **Строка, чтение** - имя файла вложения

:Comment:
  **Строка, чтение/запись** - комментарий к документу

:NeedRecipientSignature:
  **Булево, чтение/запись** - документ будет отправлен с запросом подписи получателя

:CustomDocumentId:
  **Строка, чтение/запись** - внешний идентификатор документа

:TypeNamedId:
  **Строка, чтение/запись** - строковой идентификатор типа документа

:Function:
  **Строка, чтение/запись** - идентификатор функции документа. Обязательно при отправке зашифрованных документов

:Version:
  **Строка, чтение/запись** - идентификатор версии документа. Обязательно при отправке зашифрованных документов

:WorkflowId:
  **Строка, чтение/запись** - идентификатор вида документооборота

:IsEncrypted:
  **Булево, чтение/запись** - документ будет отправлен в зашифрованном виде

:Metadata:
  :doc:`Коллекция <Collection>` **объектов** :doc:`MetadataItem <MetadataItem>` **, чтение** - метаданные документа

:Content:
  :doc:`DynamicContent <DynamicContent>` **или** :doc:`BaseContent <BaseContent>` **, чтение** - представление содержимого документа


.. rubric:: Методы

+-------------------------------------+
| |CustomDocumentToSend-AddMetadata|_ |
+-------------------------------------+

.. |CustomDocumentToSend-AddMetadata| replace:: AddMetadata()

.. _CustomDocumentToSend-AddMetadata:
.. function:: CustomDocumentToSend.AddMetadata()

  Добавляет :doc:`новый элемент <MetadataItem>` в коллекцию *Metadata* и возвращает его


.. rubric:: Дополнительная информация

Если объект был создан из :doc:`PackageSendTask2 <PackageSendTask2>`, то поле *Content* будет объектом :doc:`DynamicContent <DynamicContent>`

Если объект был создан из :doc:`PackageSendTask <PackageSendTask>` или :doc:`SendTask <SendTask>`, то поле *Content* будет объектом, производным от :doc:`BaseContent <BaseContent>`


.. seealso:: :doc:`../HowTo/HowTo_post_document`
