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
    :doc:`Коллекция <Collection>` **объектов** :doc:`DocumentMetadataItem` **, чтение** - описания метаданных документа

:EncryptedMetadataItems:
    :doc:`Коллекция <Collection>` **объектов** :doc:`DocumentMetadataItem` **, чтение** - описания метаданных для отправки зашифрованного документа

:Type:
    **Строка, чтение** - название титула для задания или получения параметров подписанта для титула через :doc:`SetExtendedSignerDetailsTask` и метод :meth:`Organization.GetExtendedSignerDetails2`

    .. versionadded:: 5.33.0


.. rubric:: Дополнительная информация

Только для титулов с ``HaveUserDataXSD == True``:
    * доступен метод :meth:`PackageSendTask2.AddDocument`.
      В противном случае, для добавления :doc:`документа на отправку <CustomDocumentToSend>` необходимо воспользоваться методом :meth:`PackageSendTask2.AddDocumentFromFile` или :meth:`PackageSendTask2.AddDocumentFromBase64`

    * доступно получение контента методом :meth:`DocumentBase.GetDynamicContent`


.. seealso:: :doc:`../HowTo/HowTo_post_document`