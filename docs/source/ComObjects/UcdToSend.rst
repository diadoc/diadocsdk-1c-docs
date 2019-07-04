UcdToSend
=========

Объект представляет собой формализованный документ на отправку "Универсальный корректировочный документ" в формате приказа `ММВ-7-15/189@ <https://normativ.kontur.ru/document?moduleId=1&documentId=273231>`_ и является производным объектом от :doc:`DocumentToSend <DocumentToSend>`.

Свойства объекта
----------------

- **Type** (строка, чтение) - тип документа (возвращает значение "UniversalCorrectionDocument")

- **Comment** (строка, чтение/запись) - комментарий к документу

- **CustomDocumentId** (строка, чтение/запись) - внешний идентификатор документа

- **Content** (:doc:`UcdSellerContent <UcdSellerContent>`, чтение) - содержимое документа
