Релиз 5.21.0
=============

.. feed-entry::
   :date: 2018-03-13

- расширена поддержка документов "любого типа":
    - у базового объекта :doc:`Document <Document>` появились новые свойства:
        - **TypeNamedId** - строковый идентификатор типа документа
        - **DocumentFunction** - функция документа 
        - **WorkflowId** - идентификатор типа документооборота
        - **Metadata** - коллекция метаданных
        - новые статусы и метаданные **RecipientReceiptMetadata**, **ConfirmationMetadata**, **RecipientResponseStatus**, **AmendmentRequestMetadata**
    - мапинг содержимого документов "любого типа" на объектную модель документов компоненты:
        - поддержка получения документов "любого типа" в представлении :doc:`BaseDocument <BaseDocument>`
        - поддержка отправки документов "любого типа" в :doc:`PackageSendTask <PackageSendTask>` - возможность добавлять объект :doc:`CustomDocumentToSend <CustomDocumentToSend>` для конкретного типа содержимого AttachmentVersion Diadoc API (поддерживаются: utd_05_01_01, utd_05_01_02, ucd_05_01_01, rezru_05_01_01, tovtorg_05_01_02)

- новое свойство **Title** у объекта :doc:`Document <Document>` - название документа
- :doc:`Исправлены ошибки <Bugs_5_21>`


`История изменений <http://diadocsdk-1c.readthedocs.io/ru/latest/History.html>`_

`Релиз <http://diadocsdk-1c.readthedocs.io/ru/latest/Downloads.html>`_