TemplateToSend
==============

Шаблон документа на отправку


.. rubric:: Свойства

:Comment:
  **Строка, чтение/запись** - необязательный текстовый комментарий к документу

:TypeNamedId:
  **Строка, чтение/запись** - строковой идентификатор типа документа

:Function:
  **Строка, чтение/запись** - идентификатор функции документа. Обязательно при отправке зашифрованных документов

:Version:
  **Строка, чтение/запись** - идентификатор версии документа. Обязательно при отправке зашифрованных документов

:Metadata:
  :doc:`Коллекция <Collection>` **объектов** :doc:`MetadataItem <MetadataItem>` **, чтение** - список пар вида «ключ-значение», содержащих метаданные документа

:WorkflowId:
  **Строка, чтение/запись** - идентификатор вида документооборота

:CustomDocumentId:
  **Строка, чтение/запись** - необязательный идентификатор документа во внешней системе

:EditingSettingId:
  **Строка, чтение/запись** - идентификатор настройки редактирования содержимого документа. Наличие данной настройки означает, что в содержимом файла может отсутствовать контент, редактирование которого разрешено данной настройкой

:NeedRecipientSignature:
  **Булево, чтение/запись** -  запрос подписи получателя под отправляемым документом, созданным из шаблона. При его проставлении документ, который будет создан из шаблона, будет требовать подпись от получателя



.. rubric:: Методы

+-------------------------------+-------------------------------------------+------------------------------------------+
| |TemplateToSend-AddMetadata|_ | |TemplateToSend-LoadSellerTitleFromFile|_ | |TemplateToSend-LoadBuyerTitleFromFile|_ |
+-------------------------------+-------------------------------------------+------------------------------------------+

.. |TemplateToSend-AddMetadata| replace:: AddMetadata()
.. |TemplateToSend-LoadSellerTitleFromFile| replace:: LoadSellerTitleFromFile()
.. |TemplateToSend-LoadBuyerTitleFromFile| replace:: LoadBuyerTitleFromFile()



.. _TemplateToSend-AddMetadata:
.. method:: TemplateToSend.AddMetadata()

  Добавляет :doc:`новый элемент <MetadataItem>` в коллекцию *Metadata* и возвращает его



.. _TemplateToSend-LoadSellerTitleFromFile:
.. method:: TemplateToSend.LoadSellerTitleFromFile(FilePath)

  :FilePath: ``строка`` путь до файла с контентом шаблона первого титула документооборота

  Добавляет контент титула продавца/отправителя из файла



.. _TemplateToSend-LoadBuyerTitleFromFile:
.. method:: TemplateToSend.LoadBuyerTitleFromFile(FilePath)

  :FilePath: ``строка`` путь до файла с контентом шаблона второго(ответного) титула документооборота

  Добавляет контент титула покупателя/получателя из файла
