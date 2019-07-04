UtdRevisionToSend
=================

Объект представляет собой формализованный документ на отправку "Исправление универсального передаточного документа" в формате приказа `ММВ-7-15/155@ <https://normativ.kontur.ru/document?moduleId=1&documentId=271958>`_ и является производным объектом от :doc:`DocumentToSend <DocumentToSend>`.

Свойства объекта
----------------

- **Type** (строка, чтение) - тип документа (возвращает значение "UniversalTrasnferDocumentRevision")

- **Comment** (строка, чтение/запись) - комментарий к документу

- **CustomDocumentId** (строка, чтение/запись) - внешний идентификатор документа

- **Content** (:doc:`UtdSellerContent <UtdSellerContent>`, чтение) - содержимое документа
