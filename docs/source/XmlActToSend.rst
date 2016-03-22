XmlActToSend
============

Объект представляет собой формализованный документ "акт о выполненных работах" на отправку 
и является производным объектом от :doc:`DocumentToSend <DocumentToSend>`.

Свойства объекта
----------------

- **Content** (чтение/запись) - содержимое документа, объект 
  :doc:`AcceptanceCertificateSellerContent <AcceptanceCertificateSellerContent>`

- **Type** (строка, чтение) - тип документа (возвращает строку "XmlAcceptanceCertificate")

- **Comment** (строка, чтение/запись) - комментарий к документу

- **CustomDocumentId** (строка, чтение/запись) - внешний идентификатор документа


Методы отсутствуют.