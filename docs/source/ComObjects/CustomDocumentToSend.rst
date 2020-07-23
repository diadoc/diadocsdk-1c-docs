CustomDocumentToSend
====================

Документ на отправку произвольного типа.
Является производным объектом от :doc:`DocumentToSend`


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
  :doc:`Коллекция <Collection>` **объектов** :doc:`MetadataItem` **, чтение** - метаданные документа

:Content:
  :doc:`DynamicContent` **или** :doc:`BaseContent` **, чтение** - представление содержимого документа.
  Если объект был создан из :doc:`PackageSendTask2`, то поле *Content* будет объектом :doc:`DynamicContent`.
  Если объект был создан из :doc:`PackageSendTask` или :doc:`SendTask`, то поле *Content* будет объектом, производным от :doc:`BaseContent`

:EditingSettingId:
  **Строка, чтение/запись** - идентификатор настройки редактирования содержимого документа.
  Наличие данной настройки означает, что в содержимом файла может отсутствовать контент, редактирование которого разрешено данной настройкой.
  В случае указания данной настройки, :doc:`отправку документов <PackageSendTask2>` необходимо выполнять с флагом *DelaySend**

  .. versionadded:: 5.29.13


.. rubric:: Методы

+-------------------------------------+--------------------------------------+
| |CustomDocumentToSend-AddMetadata|_ | |CustomDocumentToSend-SaveUserData|_ |
+-------------------------------------+--------------------------------------+

.. |CustomDocumentToSend-AddMetadata| replace:: AddMetadata()
.. |CustomDocumentToSend-SaveUserData| replace:: SaveUserData()

.. _CustomDocumentToSend-AddMetadata:
.. method:: CustomDocumentToSend.AddMetadata()

  Добавляет :doc:`новый элемент <MetadataItem>` в коллекцию *Metadata* и возвращает его


.. _CustomDocumentToSend-SaveUserData:
.. method:: CustomDocumentToSend.SaveUserData(FilePath)

  :FilePath: ``строка`` путь до файла

  Сохраняет :doc:`упрощённое представление контента <DynamicContent>` в указанный файл. Если файл не существует, то файл будет создан. Директория должна существовать



.. seealso:: :doc:`../HowTo/HowTo_post_document`
