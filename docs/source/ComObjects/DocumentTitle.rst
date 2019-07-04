DocumentTitle
=============

Объект, описывающий титул документа


.. rubric:: Свойства

:IsFormal: (булево, чтение) - титул формализованный
:XsdUrl: (строка, чтение) - адрес метода, возвращающего файл XSD-схемы
:HaveUserDataXSD: (булево, чтение) - есть ли для этого документа описание контента.
:MetadataItems: (:doc:`коллекция <Collection>` объектов :doc:`DocumentMetadataItem <DocumentMetadataItem>`, чтение) - описания метаданных документа
:EncryptedMetadataItems: (:doc:`коллекция <Collection>` объектов :doc:`DocumentMetadataItem <DocumentMetadataItem>`, чтение) - описания метаданных для отправки зашифрованного документа


.. rubric:: Дополнительная информация

* Только для титулов документа с истиной в поле **HaveUserDataXSD** доступно добавление в объект :doc:`PackageSendTask2 <PackageSendTask2>` методом :doc:`AddDocument <PackageSendTask2_AddDocument>` для последующего заполнения. В противном случае, документ можно отправить только загрузив файлом с диска
