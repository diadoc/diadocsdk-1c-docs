Релиз 5.21.0
============

.. feed-entry::
   :date: 2018-03-13

- расширена поддержка документов "любого типа":
    - у базового объекта Document появились новые свойства:
        - **TypeNamedId** - строковый идентификатор типа документа
        - **DocumentFunction** - функция документа 
        - **WorkflowId** - идентификатор типа документооборота
        - **Metadata** - коллекция метаданных
        - новые статусы и метаданные **RecipientReceiptMetadata**, **ConfirmationMetadata**, **RecipientResponseStatus**, **AmendmentRequestMetadata**
    - мапинг содержимого документов "любого типа" на объектную модель документов компоненты:
        - поддержка получения документов "любого типа" в представлении BaseDocument
        - поддержка отправки документов "любого типа" в PackageSendTask - возможность добавлять объект CustomDocumentToSend для конкретного типа содержимого AttachmentVersion Diadoc API (поддерживаются: utd_05_01_01, utd_05_01_02, ucd_05_01_01, rezru_05_01_01, tovtorg_05_01_02)

- новое свойство **Title** у объекта Document - название документа
- :doc:`Исправлены ошибки <Bugs_5_21>`


`История изменений <http://diadocsdk-1c.readthedocs.io/ru/latest/History.html>`_

`Релиз <http://diadocsdk-1c.readthedocs.io/ru/latest/Downloads.html>`_