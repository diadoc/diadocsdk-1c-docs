DocumentTitle
=============

Описание титула документа


.. rubric:: Свойства

:IsFormal:
  **Булево, чтение** - титул формализованный

:XsdUrl:
  **Строка, чтение** - адрес метода, возвращающего файл XSD-схемы титула

:HaveUserDataXSD:
  **Булево, чтение** - есть ли для этого документа упрощенное описание контента

:MetadataItems:
  :doc:`Коллекция <Collection>` **объектов** :doc:`DocumentMetadataItem <DocumentMetadataItem>` **, чтение** - описания метаданных документа

:EncryptedMetadataItems:
  :doc:`Коллекция <Collection>` **объектов** :doc:`DocumentMetadataItem <DocumentMetadataItem>` **, чтение** - описания метаданных для отправки зашифрованного документа


.. rubric:: Дополнительная информация

* Только для титулов с *HaveUserDataXSD* == ``TRUE``, доступен метод :func:`PackageSendTask2.AddDocument`.
  В противном случае, для добавления :doc:`документа на отправку <CustomDocumentToSend>` необходимо воспользоваться методом :func:`PackageSendTask2.AddDocumentFromFile` или :func:`PackageSendTask2.AddDocumentFromString`


.. seealso:: :doc:`../HowTo/HowTo_post_document`
