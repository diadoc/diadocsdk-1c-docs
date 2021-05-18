CustomDocumentToSend
====================

Документ на отправку произвольного типа.

Наследует интерфейс :doc:`DocumentToSend`


.. rubric:: Свойства

:TypeNamedId:
  **Строка, чтение/запись** - строковой идентификатор типа документа

:Function:
  **Строка, чтение/запись** - идентификатор функции документа. Обязательно при отправке зашифрованных документов

:Version:
  **Строка, чтение/запись** - идентификатор версии документа. Обязательно при отправке зашифрованных документов

:Metadata:
  :doc:`Коллекция <Collection>` **объектов** :doc:`MetadataItem` **, чтение** - метаданные документа

:WorkflowId:
  **Строка, чтение/запись** - идентификатор вида документооборота

:EditingSettingId:
  **Строка, чтение/запись** - идентификатор настройки редактирования содержимого документа.
  Наличие данной настройки означает, что в содержимом файла может отсутствовать контент, редактирование которого разрешено данной настройкой.
  В случае указания данной настройки, :doc:`отправку документов <PackageSendTask2>` необходимо выполнять с флагом *DelaySend**

  .. versionadded:: 5.29.13

:Type:
  **Строка, чтение** - тип документа. Константа ``Document``

:Content:
  :doc:`DynamicContent` **, чтение** - представление содержимого документа.
  Если контент документа был загружен с диска, то поле будет :doc:`пустым <Descriptions/Empty_Com_Object>`.
  Для документов, для которых не существует упрощённого представления контента (см. :doc:`../HowTo/HowTo_post_document`), поле будет :doc:`пустым <Descriptions/Empty_Com_Object>`




.. rubric:: Методы

+--------------------------------------+
| |CustomDocumentToSend-AddMetadata|_  |
+--------------------------------------+
| |CustomDocumentToSend-SaveUserData|_ |
+--------------------------------------+

.. |CustomDocumentToSend-AddMetadata| replace:: AddMetadata()
.. |CustomDocumentToSend-SaveUserData| replace:: SaveUserData()

.. _CustomDocumentToSend-AddMetadata:
.. method:: CustomDocumentToSend.AddMetadata()

  Добавляет :doc:`новый элемент <MetadataItem>` в коллекцию *Metadata* и возвращает его


.. _CustomDocumentToSend-SaveUserData:
.. method:: CustomDocumentToSend.SaveUserData(FilePath)

  :FilePath: ``строка`` путь до файла

  Сохраняет :doc:`упрощённое представление контента <DynamicContent>` в указанный файл.
  Если файл не существует, то файл будет создан.
  Директория должна существовать



.. seealso:: :doc:`../HowTo/HowTo_post_document`
